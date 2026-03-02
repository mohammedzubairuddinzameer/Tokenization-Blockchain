import hashlib
import json
import time

LEDGER_FILE = "data/ledger.json"

def load_ledger():
    try:
        with open(LEDGER_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_ledger(ledger):
    with open(LEDGER_FILE, "w") as f:
        json.dump(ledger, f, indent=4)

def calculate_hash(block):
    block_string = json.dumps(block, sort_keys=True)
    return hashlib.sha256(block_string.encode()).hexdigest()

def create_genesis_block():
    return {
        "index": 0,
        "timestamp": time.time(),
        "data": "Genesis Block",
        "previous_hash": "0"
    }

def add_block(data):
    ledger = load_ledger()

    if len(ledger) == 0:
        genesis = create_genesis_block()
        genesis["hash"] = calculate_hash(genesis)
        ledger.append(genesis)

    last_block = ledger[-1]

    new_block = {
        "index": len(ledger),
        "timestamp": time.time(),
        "data": data,
        "previous_hash": last_block["hash"]
    }

    new_block["hash"] = calculate_hash(new_block)
    ledger.append(new_block)

    save_ledger(ledger)
