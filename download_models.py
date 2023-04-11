# Download whisper models for bundling.

import os
import requests
import sys
import whisper
import xdg

# Define root path
PATH = xdg.xdg_cache_home() / "whisper"

# Ensure that the parent directory exists
os.makedirs(PATH)

# Download one by one
for model in sys.argv[1:]:
    with open(PATH / f"{model}.pt", "wb") as mfile:
        mfile.write(requests.get(whisper._MODELS[model]).content)
