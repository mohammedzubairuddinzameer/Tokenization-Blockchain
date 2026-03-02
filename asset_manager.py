import json
import uuid

def load_data(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def register_asset(name, owner, value):
    assets = load_data("data/assets.json")
    asset_id = str(uuid.uuid4())
    assets.append({
        "asset_id": asset_id,
        "name": name,
        "owner": owner,
        "value": value
    })
    save_data("data/assets.json", assets)
    return asset_id
