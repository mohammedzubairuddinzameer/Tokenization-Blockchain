import streamlit as st
from blockchain import create_block
from asset_manager import register_asset, load_data, save_data

st.set_page_config(page_title="Asset Tokenization Blockchain")

st.title("🔗 Blockchain Asset Tokenization System")

menu = st.sidebar.selectbox("Menu", [
    "Register Asset",
    "View Assets",
    "Blockchain Ledger"
])

if menu == "Register Asset":
    st.subheader("Register New Asset")
    name = st.text_input("Asset Name")
    owner = st.text_input("Owner Name")
    value = st.number_input("Asset Value", min_value=0)

    if st.button("Register"):
        asset_id = register_asset(name, owner, value)
        st.success(f"Asset Registered with ID: {asset_id}")

elif menu == "View Assets":
    st.subheader("Registered Assets")
    assets = load_data("data/assets.json")
    st.json(assets)

elif menu == "Blockchain Ledger":
    st.subheader("Blockchain Ledger")
    ledger = load_data("data/ledger.json")
    st.json(ledger)
