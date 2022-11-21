import sys

from whisper.transcribe import cli


if __name__ == "__main__":
    # If this was called without arguments, we fire the GUI.
    # Otherwise, we use whisper's CLI.
    if len(sys.argv) == 1:
        print("GUI")
    else:
        cli()
