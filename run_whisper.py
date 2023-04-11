import os
import psutil
import sys
import torch
import tqdm
import whisper
import xdg

from torch import cuda

from whisper import load_model
from whisper.transcribe import cli, transcribe

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFileDialog,
    QProgressBar,
    QPushButton,
    QLineEdit,
    QGroupBox,
    QComboBox,
    QPlainTextEdit,
)


# The list of available whisper models
_models = {
    "Tiny Model (english only)": ("tiny.en", 1.1e9),
    "Tiny Model": ("tiny", 1.1e9),
    "Base Model (english only)": ("base.en", 1.1e9),
    "Base Model": ("base", 1.1e9),
    "Small Model (english only)": ("small.en", 2.2e9),
    "Small Model": ("small", 2.2e9),
    "Medium Model (english only)": ("medium.en", 5.5e9),
    "Medium Model": ("medium", 5.5e9),
    "Large Model": ("large", 1.1e10),
}


class FileSelectionWidget(QGroupBox):
    def __init__(self, default="", title=""):
        super(FileSelectionWidget, self).__init__(title)

        layout = QHBoxLayout()
        self._input = QLineEdit(default)
        layout.addWidget(self._input)

        button = QPushButton("Choose")

        def select():
            self._input.setText(
                QFileDialog.getOpenFileName(self, f"Choose {title}", os.getcwd())[0]
            )

        button.clicked.connect(select)
        layout.addWidget(button)

        self.setLayout(layout)

    @property
    def filename(self):
        return self._input.text()


class WhisperWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(WhisperWindow, self).__init__(*args, **kwargs)
        layout = QVBoxLayout()

        # Sound input
        self.input = FileSelectionWidget(default="input.wav", title="Input Sound File")
        layout.addWidget(self.input)

        # Language model selection
        language_group = QGroupBox("Language Model")
        language_layout = QVBoxLayout()

        # Model selection dropdown
        self.cb = QComboBox()
        available_mem = psutil.virtual_memory().available
        omitted = False
        for model, (_, mem) in _models.items():
            if mem < available_mem:
                self.cb.addItem(model)
            else:
                omitted = True
        self.cb.setCurrentText("Base Model")
        language_layout.addWidget(self.cb)
        if omitted:
            language_layout.addWidget(
                QLabel(
                    "One or more models were omitted because the available RAM on this computer is not sufficient to run them."
                )
            )
        language_group.setLayout(language_layout)
        layout.addWidget(language_group)

        # Run Button
        run_group = QGroupBox("Running the model")
        run_layout = QVBoxLayout()
        self.run_button = QPushButton("Transcribe")

        self.device = QComboBox()
        for i in range(cuda.device_count()):
            self.device.addItem(cuda.get_device_name(i))
        self.device.addItem("CPU")

        self.progressbar = QProgressBar()
        self.progressbar.hide()

        self.run_button.clicked.connect(self.transcribe)
        run_layout.addWidget(self.device)
        run_layout.addWidget(self.progressbar)
        run_layout.addWidget(self.run_button)
        run_group.setLayout(run_layout)
        layout.addWidget(run_group)

        # Output group
        self.output_group = QGroupBox()
        output_layout = QVBoxLayout()

        self.outputfield = QPlainTextEdit()
        self.outputfield.setReadOnly(True)

        copytoclipboard = QPushButton("Copy to clipboard")
        copytoclipboard.clicked.connect(
            lambda: QApplication.clipboard().setText(self.outputfield.toPlainText())
        )

        output_layout.addWidget(copytoclipboard)
        output_layout.addWidget(self.outputfield)

        self.output_group.hide()
        self.output_group.setLayout(output_layout)
        self.output_group.setWindowTitle("Transcription Results")

        # Finalize
        self.setLayout(layout)
        self.setWindowTitle("Whisper Transcription")

    def transcribe(self):
        # Disable the button while we are processing
        self.run_button.setEnabled(False)

        # Hide previously generated output
        self.output_group.hide()

        # Make the progress bar visible
        self.progressbar.reset()
        self.progressbar.show()

        # Set the correct device
        if self.device.currentIndex() == cuda.device_count():
            dev = torch.device("cpu")
        else:
            dev = torch.device(f"cuda:{self.device.currentIndex()}")

        def monkeypatching_tqdm(progressbar, format):
            def _monkeypatching_tqdm(
                total=None,
                ncols=None,
                unit=None,
                unit_scale=True,
                unit_divisor=None,
                disable=False,
            ):
                class TqdmMonkeypatchContext:
                    def __enter__(self):
                        return self

                    def __exit__(self, *args):
                        pass

                    def update(self, value):
                        if unit_divisor:
                            value = value / unit_divisor
                        progressbar.setValue(progressbar.value() + value)
                        # This is ugly, but until we properly offload to a worker thread
                        # it prevents the GUI from freezing.
                        QApplication.instance().processEvents()

                if unit_divisor:
                    total = total / unit_divisor

                self.progressbar.reset()
                self.progressbar.setFormat(format)
                self.progressbar.setMaximum(total)

                return TqdmMonkeypatchContext()

            return _monkeypatching_tqdm

        tqdm.tqdm = monkeypatching_tqdm(self.progressbar, "Transcribing audio: %p%")
        whisper.tqdm = monkeypatching_tqdm(self.progressbar, "Downloading model: %p%")

        # Show intermediate message on the progress bar
        self.progressbar.reset()
        self.progressbar.setFormat("Preparing model loading...")
        self.progressbar.setMaximum(1)
        self.progressbar.setValue(0)

        # Load the selected model
        model = self.cb.currentText()
        model = load_model(
            _models[model][0],
            download_root=xdg.xdg_cache_home() / "whisper",
            device=dev,
        )

        # Show intermediate message on the progress bar
        self.progressbar.reset()
        self.progressbar.setFormat("Preparing transcription...")
        self.progressbar.setMaximum(1)
        self.progressbar.setValue(0)

        # Trigger transcription
        ret = transcribe(model, self.input.filename)

        # Show output
        self.outputfield.setPlainText(ret["text"])
        self.output_group.show()

        # Hide the progress bar again and reset it
        self.progressbar.hide()

        # Re-enable the run button
        self.run_button.setEnabled(True)


def gui():
    # Setup
    app = QApplication([])
    window = WhisperWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    # If this was called without arguments, we fire the GUI.
    # Otherwise, we use whisper's CLI.
    if len(sys.argv) == 1:
        gui()
    else:
        cli()
