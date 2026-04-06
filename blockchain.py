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

    block = {
        "data": data,
        "previous_hash": previous_hash,
        "timestamp": time.time()
    }

    block["hash"] = calculate_hash(block)

    supabase.table("ledger").insert(block).execute()

def get_ledger():
    response = supabase.table("ledger").select("*").execute()
    return response.data
