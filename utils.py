import json
import os

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def save_data(data, filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def load_data(filename, default=[]):
    path = os.path.join(DATA_DIR, filename)
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return default

