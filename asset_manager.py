import json
import uuid
from blockchain import add_block

ASSET_FILE = "data/assets.json"
TOKEN_FILE = "data/tokens.json"

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

    add_block({
        "action": "ASSET_REGISTERED",
        "asset": asset
    })

    return asset_id

def tokenize_asset(asset_id, total_tokens, owner):
    tokens = load_data(TOKEN_FILE)

    for i in range(total_tokens):
        tokens.append({
            "token_id": str(uuid.uuid4()),
            "asset_id": asset_id,
            "owner": owner,
            "percentage": round(100 / total_tokens, 2)
        })

    save_data(TOKEN_FILE, tokens)

    add_block({
        "action": "ASSET_TOKENIZED",
        "asset_id": asset_id,
        "total_tokens": total_tokens
    })

def transfer_token(token_id, new_owner):
    tokens = load_data(TOKEN_FILE)

    for token in tokens:
        if token["token_id"] == token_id:
            old_owner = token["owner"]
            token["owner"] = new_owner

            save_data(TOKEN_FILE, tokens)

            add_block({
                "action": "TOKEN_TRANSFER",
                "token_id": token_id,
                "from": old_owner,
                "to": new_owner
            })
            return True

    return False
