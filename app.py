import streamlit as st
from asset_manager import (
    register_asset,
    get_assets,
    tokenize_asset,
    get_tokens,
    transfer_token
)
from blockchain import get_ledger, validate_blockchain

st.set_page_config(page_title="Asset Tokenization Blockchain")

st.title("🔗 Blockchain Asset Tokenization System")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Register Asset",
        "View Assets",
        "Tokenize Asset",
        "View Tokens",
        "Transfer Token",
        "Blockchain Ledger",
        "Validate Blockchain" 
    ]
)

if menu == "Register Asset":
    st.subheader("Register New Asset")

    name = st.text_input("Asset Name")
    owner = st.text_input("Owner Name")
    value = st.number_input("Asset Value", min_value=0)

    if st.button("Register Asset"):
        if name and owner and value > 0:
            asset_id = register_asset(name, owner, value)
            st.success(f"Asset registered successfully!")
            st.code(id)
        else:
            st.warning("Please fill all fields correctly.")

elif menu == "View Assets":
    st.subheader("Registered Assets")
    assets = get_assets()
    if len(assets) == 0:
        st.info("No assets registered yet.")
    else:
        st.json(assets)

elif menu == "Tokenize Asset":
    st.subheader("Tokenize Asset")

    assets = get_assets()

    if len(assets) == 0:
        st.warning("No assets available")
    else:
        asset_ids = [a["id"] for a in assets]
        asset_id = st.selectbox("Select Asset ID", asset_ids)
        owner = st.text_input("Owner Name")
        total_tokens = st.number_input("Number of Tokens", min_value=1)

        if st.button("Tokenize"):
            tokenize_asset(asset_id, total_tokens, owner)
            st.success("Asset tokenized successfully")

elif menu == "View Tokens":
    st.subheader("Tokenized Assets")
    tokens = get_tokens()

    if len(tokens) == 0:
        st.info("No tokens created yet")
    else:
        st.json(tokens)

elif menu == "Transfer Token":
    st.subheader("Transfer Token Ownership")

    tokens = get_tokens()

    if len(tokens) == 0:
        st.warning("No tokens available")
    else:
        token_ids = [t["token_id"] for t in tokens]
        token_id = st.selectbox("Select Token ID", token_ids)
        new_owner = st.text_input("New Owner Name")

        if st.button("Transfer"):
            success = transfer_token(token_id, new_owner)
            if success:
                st.success("Token transferred successfully")
            else:
                st.error("Transfer failed")
                
elif menu == "Blockchain Ledger":
    st.subheader("Blockchain Ledger")
    ledger = get_ledger()
    if len(ledger) == 0:
        st.info("Blockchain ledger is empty.")
    else:
        st.json(ledger)

elif menu == "Validate Blockchain":
    st.subheader("🔍 Blockchain Validation")

    if st.button("Check Integrity"):
        valid, message = validate_blockchain()

        if valid:
            st.success(message)
        else:
            st.error(message)
