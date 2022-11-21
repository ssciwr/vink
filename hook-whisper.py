from PyInstaller.utils.hooks import collect_data_files, copy_metadata

# The transformers package inspects metadata of its dependencies
datas = copy_metadata("transformers", recursive=True)

# We explicitly bundle whisper assets
datas += collect_data_files("whisper", subdir="assets")
