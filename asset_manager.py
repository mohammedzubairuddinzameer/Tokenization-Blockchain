from db import supabase
import uuid
from blockchain import add_block
import hashlib

def generate_file_hash(file):
    file_bytes = file.read()
    return hashlib.sha256(file_bytes).hexdigest()
    
def register_asset(name, owner, value, user_id, visibility, shared_with):
    asset_id = str(uuid.uuid4())

    asset = {
        "id": asset_id,
        "name": name,
        "owner": owner,
        "value": value,
        "user_id": user_id,
        "visibility": visibility,
        "shared_with": shared_with
    }

    supabase.table("assets").insert(asset).execute()

    add_block({
        "action": "ASSET_REGISTERED",
        "asset": asset
    })

    return asset_id


def get_assets(user_id, username):
    response = supabase.table("assets").select("*").execute()
    all_assets = response.data

    visible_assets = []

    for asset in all_assets:
        visibility = asset.get("visibility", "private")

        if visibility == "public":
            visible_assets.append(asset)

        elif asset.get("user_id") == user_id:
            visible_assets.append(asset)

        elif visibility == "shared":
            shared_with = asset.get("shared_with", "")
            if username in shared_with:
                visible_assets.append(asset)

    return visible_assets


def tokenize_asset(asset_id, total_tokens, owner):
    tokens = []

    for i in range(total_tokens):
        tokens.append({
            "token_id": str(uuid.uuid4()),
            "asset_id": asset_id,
            "owner": owner,
            "percentage": round(100 / total_tokens, 2)
        })

    supabase.table("tokens").insert(tokens).execute()

    add_block({
        "action": "ASSET_TOKENIZED",
        "asset_id": asset_id
    })


def get_tokens():
    response = supabase.table("tokens").select("*").execute()
    return response.data


def transfer_token(token_id, new_owner):
    tokens = get_tokens()

    for token in tokens:
        if token["token_id"] == token_id:
            old_owner = token["owner"]

            supabase.table("tokens").update({
                "owner": new_owner
            }).eq("token_id", token_id).execute()

            add_block({
                "action": "TOKEN_TRANSFER",
                "token_id": token_id,
                "from": old_owner,
                "to": new_owner
            })

            return True

    return False
