import json
import uuid
from blockchain import add_block

ASSET_FILE = "data/assets.json"

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
    assets = load_data(ASSET_FILE)

    asset_id = str(uuid.uuid4())

    asset = {
        "asset_id": asset_id,
        "name": name,
        "owner": owner,
        "value": value
    }

    assets.append(asset)
    save_data(ASSET_FILE, assets)

    # 🔗 ADD TO BLOCKCHAIN
    add_block({
        "action": "ASSET_REGISTERED",
        "asset": asset
    })

    return asset_id
