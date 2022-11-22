# This hook downloads the FFmpeg executable in order to bundle it into ffmpeg-python.
# The reason this is done is that we need to absolutely ensure that the bundled executable
# complied with LGPL, because FFmpeg also contains GPL parts.

from PyInstaller.compat import is_win, is_linux

import os
import requests
import shutil
import tarfile
import tempfile
import zipfile

LINUX_URL = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n5.1-latest-linux64-lgpl-5.1.tar.xz"
WINDOWS_URL = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n5.1-latest-win64-lgpl-5.1.zip"

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

        datas = [os.path.join(os.getwcd(), "ffmpeg.exe")]

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
