from pathlib import Path
import json

def GetConfig():
    config = json.load(open(Path(__file__).resolve().parent.parent / "config.json", "r"))

    return config