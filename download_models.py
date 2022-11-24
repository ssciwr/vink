# Download whisper models for bundling.

import os
import requests
import sys
import whisper

# Ensure that the parent directory exists
os.makedirs("whisper_models")

# Download one by one
for model in sys.argv[1:]:
    mpath = os.path.join(os.getcwd(), "whisper_models", f"{model}.pt")
    with open(mpath, "wb") as mfile:
        mfile.write(requests.get(whisper._MODELS[model]).content)
