import streamlit as st
from asset_manager import register_asset, load_data
from blockchain import load_ledger

st.set_page_config(page_title="Asset Tokenization Blockchain")

st.title("🔗 Blockchain Asset Tokenization System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Register Asset", "View Assets", "Blockchain Ledger"]
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
            st.code(asset_id)
        else:
            st.warning("Please fill all fields correctly.")

elif menu == "View Assets":
    st.subheader("Registered Assets")
    assets = load_data("data/assets.json")
    if len(assets) == 0:
        st.info("No assets registered yet.")
    else:
        st.json(assets)

elif menu == "Blockchain Ledger":
    st.subheader("Blockchain Ledger")
    ledger = load_ledger()
    if len(ledger) == 0:
        st.info("Blockchain ledger is empty.")
    else:
        st.json(ledger)
