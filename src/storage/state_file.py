import json, os
def save_state(path: str, data: dict):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w') as f: json.dump(data, f)
