from PyInstaller.utils.hooks import collect_data_files

# We explicitly bundle whisper assets
datas = collect_data_files("whisper", subdir="assets")
