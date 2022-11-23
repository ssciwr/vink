import sys

from whisper.transcribe import cli

from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFileDialog,
    QPushButton,
    QLineEdit,
    QGroupBox,
    QComboBox,
)


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


def transcribe(*args):
    print(args)


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
    cb = QComboBox()
    for model in ["a", "b"]:
        cb.addItem(model)
    language_layout.addWidget(cb)
    language_group.setLayout(language_layout)
    layout.addWidget(language_group)

    # Run Button
    run_button = QPushButton("&Transcribe")
    run_button.clicked.connect(
        lambda: transcribe(input.filename, output.filename, cb.currentText())
    )
    layout.addWidget(run_button)

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
