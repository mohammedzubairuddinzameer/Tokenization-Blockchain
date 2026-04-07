import hashlib
import json
import time
from db import supabase

def calculate_hash(block):
    block_string = json.dumps(block, sort_keys=True)
    return hashlib.sha256(block_string.encode()).hexdigest()

def get_last_block():
    response = supabase.table("ledger").select("*").order("id", desc=True).limit(1).execute()
    data = response.data
    return data[0] if data else None

def add_block(data):
    last_block = get_last_block()

    previous_hash = last_block["hash"] if last_block else "0"

    # 🔥 STANDARD STRUCTURE (ONLY THESE FIELDS)
    block = {
        "data": data,
        "previous_hash": previous_hash,
        "timestamp": round(time.time(), 6)  # fix precision
    }

    # calculate hash ONLY on this structure
    block_hash = calculate_hash(block)

    # store clean block + hash
    db_block = {
        "data": block["data"],
        "previous_hash": block["previous_hash"],
        "timestamp": block["timestamp"],
        "hash": block_hash
    }

    supabase.table("ledger").insert(db_block).execute()

def get_ledger():
    response = supabase.table("ledger").select("*").execute()
    return response.data

def validate_blockchain():
    ledger = get_ledger()

    if not ledger:
        return True, "Blockchain is empty"

    for i in range(len(ledger)):
        current = ledger[i]

        # 🔥 Recreate EXACT SAME STRUCTURE
        block = {
            "data": current["data"],
            "previous_hash": current["previous_hash"],
            "timestamp": current["timestamp"]
        }

        recalculated_hash = calculate_hash(block)

        if current["hash"] != recalculated_hash:
            return False, f"Block {i} has been tampered!"

        if i > 0:
            previous = ledger[i - 1]
            if current["previous_hash"] != previous["hash"]:
                return False, f"Chain broken at block {i}!"

    return True, "Blockchain is valid"
