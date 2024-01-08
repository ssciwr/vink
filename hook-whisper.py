from PyInstaller.compat import is_win, is_linux
from PyInstaller.utils.hooks import collect_data_files

import os
import requests
import shutil
import tarfile
import tempfile
import zipfile

LINUX_URL = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n5.1-latest-linux64-lgpl-5.1.tar.xz"
WINDOWS_URL = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n5.1-latest-win64-lgpl-5.1.zip"

# We explicitly bundle whisper assets
datas = collect_data_files("whisper", subdir="assets")

# We also bundle ffmpeg as it is called by whisper
if is_win:
    with tempfile.TemporaryDirectory() as tmp_dir:
        with open(os.path.join(tmp_dir, "ffmpeg.zip"), "wb") as zip:
            zip.write(requests.get(WINDOWS_URL).content)

        with zipfile.ZipFile(os.path.join(tmp_dir, "ffmpeg.zip"), mode="r") as zip:
            zip.extractall(path=tmp_dir)

        shutil.copy(
            os.path.join(
                tmp_dir, "ffmpeg-n5.1-latest-win64-lgpl-5.1", "bin", "ffmpeg.exe"
            ),
            os.getcwd(),
        )

        datas = [(os.path.join(os.getcwd(), "ffmpeg.exe"), ".")]

if is_linux:
    with tempfile.TemporaryDirectory() as tmp_dir:
        with open(os.path.join(tmp_dir, "ffmpeg.tar.xz"), "wb") as tar:
            tar.write(requests.get(LINUX_URL).content)

        with tarfile.open(os.path.join(tmp_dir, "ffmpeg.tar.xz"), "r:xz") as tar:
            tar.extractall(path=tmp_dir)

        shutil.copy(
            os.path.join(
                tmp_dir, "ffmpeg-n5.1-latest-linux64-lgpl-5.1", "bin", "ffmpeg"
            ),
            os.getcwd(),
        )

        datas = [(os.path.join(os.getcwd(), "ffmpeg"), ".")]
