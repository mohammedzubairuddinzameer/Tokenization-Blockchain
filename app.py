import streamlit as st
from asset_manager import (
    register_asset,
    get_assets,
    tokenize_asset,
    get_tokens,
    transfer_token
)
from blockchain import get_ledger, validate_blockchain
from datetime import datetime
import pytz

st.set_page_config(page_title="Asset Tokenization Blockchain")

st.title("🔗 Blockchain Asset Tokenization System")

st.markdown("""
<style>
.block-card {
    padding: 15px;
    border-radius: 10px;
    background-color: #0e1117;
    border: 1px solid #444;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

from auth import signup, login

if "user" not in st.session_state:
    st.session_state.user = None


if st.session_state.user is None:
    st.title("🔐 Login / Signup")

    option = st.radio("Select Option", ["Login", "Signup"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if option == "Signup":
        if st.button("Create Account"):
            user_id = signup(username, password)
            st.success("Account created. Please login.")

    else:
        if st.button("Login"):
            user = login(username, password)

            if user:
                st.session_state.user = user
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    st.stop()
st.sidebar.write(f"Logged in as: {st.session_state.user['username']}")

if st.sidebar.button("Logout"):
    st.session_state.user = None
    st.rerun()    
def format_timestamp(ts):
    ist = pytz.timezone("Asia/Kolkata")
    return datetime.fromtimestamp(ts, ist).strftime("%d-%m-%Y %H:%M:%S")
    
menu = st.sidebar.selectbox(
    "Menu",
    [
        "Register Asset",
        "View Assets",
        "Tokenize Asset",
        "View Tokens",
        "Transfer Token",
        "Blockchain Ledger"
    ]
)
    
if menu == "Register Asset":
    st.subheader("Register New Asset")

    name = st.text_input("Asset Name")
    owner = st.text_input("Owner Name")
    value = st.number_input("Asset Value", min_value=0)
    
    if st.button("Register Asset"):
        if menu == "Register Asset":
            if st.session_state.role != "admin":
                st.error("Access Denied")
                st.stop()
        if name and owner and value > 0:
            asset_id = register_asset(
                name,
                owner,
                value,
                st.session_state.user["id"]
            )
            st.success(f"Asset registered successfully!")
            st.code(id)
        else:
            st.warning("Please fill all fields correctly.")

elif menu == "View Assets":
    st.subheader("Registered Assets")
    assets = get_assets(st.session_state.user["id"])
    if len(assets) == 0:
        st.info("No assets registered yet.")
    else:
        st.json(assets)

elif menu == "Tokenize Asset":
    st.subheader("Tokenize Asset")

    assets = get_assets(st.session_state.user["id"])
    if menu == "Tokenize Asset":
        if st.session_state.role != "admin":
            st.error("Access Denied")
            st.stop()
            
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
    if menu == "Transfer Token":
        if st.session_state.role != "admin":
            st.error("Access Denied")
            st.stop()
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
    st.subheader("🔗 Blockchain Explorer")

    ledger = get_ledger()

    if not ledger:
        st.info("No blocks in blockchain yet.")
    else:
        for i, block in enumerate(ledger):
            with st.container():
                if i == 0:
                    st.markdown("## 🟢 Genesis Block")
                else:
                    st.markdown(f"## 🔵 Block {i}")

                st.subheader("🔗 Chain Flow")

                chain = " → ".join([f"Block {i}" for i in range(len(ledger))])
                st.success(chain)
                st.write("🕒 Time:", format_timestamp(block["timestamp"]))

                st.write("📦 Data:")
                st.json(block["data"])

                st.write("🔗 Previous Hash:")
                st.code(block["previous_hash"])

                st.write("🔐 Current Hash:")
                st.code(block["hash"])

                st.divider()

elif menu == "Validate Blockchain":
    st.subheader("🔍 Blockchain Validation")

    if st.button("Check Integrity"):
        valid, message = validate_blockchain()

        if valid:
            st.success(message)
        else:
            st.error(message)
