import os
import psutil
import sys
import torch

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
    QPushButton,
    QLineEdit,
    QGroupBox,
    QComboBox,
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


def gui():
    # Setup
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()

    # Sound input
    input = FileSelectionWidget(default="input.wav", title="Input Sound File")
    layout.addWidget(input)

    # Text output
    output = FileSelectionWidget(default="output.txt", title="Output Text File")
    layout.addWidget(output)

    # Language model selection
    language_group = QGroupBox("Language Model")
    language_layout = QVBoxLayout()

    # Model selection dropdown
    cb = QComboBox()
    available_mem = psutil.virtual_memory().available
    omitted = False
    for model, (_, mem) in _models.items():
        if mem < available_mem:
            cb.addItem(model)
        else:
            omitted = True
    cb.setCurrentText("Base Model")
    language_layout.addWidget(cb)
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
    run_button = QPushButton("Transcribe")

    device = QComboBox()
    device.addItem("CPU")
    for i in range(cuda.device_count()):
        device.addItem(cuda.get_device_name(i))

    def _transcribe():
        # Set the correct device
        dev = device.currentIndex() - 1
        if dev < 0:
            dev = torch.device("cpu")
        else:
            dev = torch.device(f"cuda:{dev}")

        # Load the selected model
        model = cb.currentText()
        model = load_model(
            _models[model][0],
            download_root=os.path.join(os.path.dirname(__file__), "whisper_models"),
            device=dev,
        )

        # Trigger transcription
        ret = transcribe(model, input.filename)

        # Write results to chosen output file
        with open(output.filename, "w") as f:
            f.write(ret["text"])

    run_button.clicked.connect(_transcribe)
    run_layout.addWidget(device)
    run_layout.addWidget(run_button)
    run_group.setLayout(run_layout)
    layout.addWidget(run_group)

    # Finalize
    window.setLayout(layout)
    window.show()
    app.exec()


if __name__ == "__main__":
    # If this was called without arguments, we fire the GUI.
    # Otherwise, we use whisper's CLI.
    if len(sys.argv) == 1:
        gui()
    else:
        cli()
