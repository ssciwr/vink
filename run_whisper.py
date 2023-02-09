import codecs
import os
import psutil
import sys
import torch
import tqdm
import traceback

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
    QProgressDialog,
    QPushButton,
    QLineEdit,
    QGroupBox,
    QComboBox,
)

from PySide6.QtCore import (
    QObject,
    QRunnable,
    Signal,
    Slot,
    QThreadPool,
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


class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    """

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    """
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    """

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs["progress_callback"] = self.signals.progress

    @Slot()
    def run(self):
        """
        Initialise the runner function with passed args, kwargs.
        """

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


class TqdmCompatibilityStatusBar:
    def __init__(self, progress_callback):
        self.progress_callback = progress_callback

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def update(self, value):
        self.progress_callback.emit(value)


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
        self.threadpool = QThreadPool()
        layout = QVBoxLayout()

        # Sound input
        self.input = FileSelectionWidget(default="input.wav", title="Input Sound File")
        layout.addWidget(self.input)

        # Text output
        self.output = FileSelectionWidget(
            default="output.txt", title="Output Text File"
        )
        layout.addWidget(self.output)

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
        run_button = QPushButton("Transcribe")

        self.device = QComboBox()
        self.device.addItem("CPU")
        for i in range(cuda.device_count()):
            self.device.addItem(cuda.get_device_name(i))

        run_button.clicked.connect(self.transcribe_spawn)
        run_layout.addWidget(self.device)
        run_layout.addWidget(run_button)
        run_group.setLayout(run_layout)
        layout.addWidget(run_group)

        # Finalize
        self.setLayout(layout)

    def transcribe(self, progress_callback=None):
        # Set the correct device
        dev = self.device.currentIndex() - 1
        if dev < 0:
            dev = torch.device("cpu")
        else:
            dev = torch.device(f"cuda:{dev}")

        # Load the selected model
        model = self.cb.currentText()
        model = load_model(
            _models[model][0],
            download_root=os.path.join(os.path.dirname(__file__), "whisper_models"),
            device=dev,
        )

        def tqdm_dropin(total=None, unit=None, disable=False):
            self.dialog = QProgressDialog(
                "Transcribing audio...", "Cancel", 0, total, None
            )
            return TqdmCompatibilityStatusBar(progress_callback)

        # Monkeypatch tqdm
        import tqdm

        tqdm.tqdm = tqdm_dropin

        # Trigger transcription
        ret = transcribe(model, self.input.filename)

        # Write results to chosen output file
        with codecs.open(self.output.filename, "w", "utf-8") as f:
            f.write(ret["text"])

    def progress_callback(self, n):
        self.dialog.setValue(self.dialog.value() + n)

    def transcribe_spawn(self):
        worker = Worker(self.transcribe)
        worker.signals.progress.connect(self.progress_callback)
        worker.signals.finished.connect(lambda: self.dialog.close())
        self.threadpool.start(worker)


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
