import hashlib
import json
import time

def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def create_block(previous_hash, data):
    block = {
        "timestamp": time.time(),
        "data": data,
        "previous_hash": previous_hash
    }
    block_string = json.dumps(block, sort_keys=True)
    block["hash"] = calculate_hash(block_string)
    return block
