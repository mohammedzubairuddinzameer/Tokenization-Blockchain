# Tokenization-Blockchain

# Blockchain-Based Tokenization of Real-World Assets

This project demonstrates how **real-world assets** such as property, gold, and certificates can be **digitally tokenized using blockchain principles**.  
It simulates a blockchain ledger using cryptographic hashing and provides **fractional ownership, transparent transfers, and immutable records**.

The application is built using **Python and Streamlit** and deployed as a web application.

---

## 🔍 Problem Addressed

Traditional asset management systems are:
- Centralized
- Prone to fraud and data manipulation
- Slow in ownership transfer
- Difficult to divide into fractional ownership

This project solves these issues by using **blockchain concepts** like decentralization, hashing, and immutable ledgers.

---

## 🚀 Features

- Register real-world assets
- Tokenize assets into fractional ownership
- Transfer token ownership
- Blockchain ledger with hash chaining
- Genesis block implementation
- Transparent and verifiable transaction history
- Streamlit-based interactive UI
- Cloud deployment ready

---

## 🛠️ Technology Stack

- **Python 3**
- **Streamlit**
- **SHA-256 Cryptographic Hashing**
- **JSON-based Ledger Storage**
- **GitHub + Streamlit Cloud**

---

## 📁 Project Structure


tokenization-blockchain/
│
├── app.py
├── blockchain.py
├── asset_manager.py
├── requirements.txt
├── README.md
│
└── data/
├── assets.json
├── tokens.json
└── ledger.json

---


## ⚙️ Installation & Setup (Local)

1. Clone the repository:
   git clone https://github.com/mohammedzubairuddinzameer/tokenization-blockchain.git

2. Install dependencies:
    pip install -r requirements.txt

3. Run the application:
    streamlit run app.py
---

## 🌐 Deployment (Streamlit Cloud)

1. Push the project to GitHub
2. Go to https://streamlit.io/cloud
3. Connect your GitHub repository
4. Select `app.py` as the main file
5. Deploy the app

---

## 🧭 How to Use the Application (With Examples)

### 1️⃣ Register Asset

Navigate to **Register Asset** from the sidebar.

**Example Input:**
- Asset Name:  
`2BHK Residential Flat – Mehdipatnam, Hyderabad`
- Owner Name:  
`Zubair Khan`
- Asset Value:  
`5500000`

**What happens:**
- A unique Asset ID is generated
- Asset is stored in `assets.json`
- A new blockchain block is created for this registration

---

### 2️⃣ View Assets

Navigate to **View Assets**.

**You will see:**
- Asset ID
- Asset name
- Owner
- Asset value

This ensures **transparency and verification**.

---

### 3️⃣ Tokenize Asset

Navigate to **Tokenize Asset**.

**Example Input:**
- Asset ID:  
(Select from dropdown)
- Owner Name:  
`Zubair Khan`
- Number of Tokens:  
`10`

**What happens:**
- Asset is divided into 10 tokens
- Each token represents **10% ownership**
- Tokens are stored in `tokens.json`
- Blockchain records the tokenization event

---

### 4️⃣ View Tokens

Navigate to **View Tokens**.

**You will see:**
- Token ID
- Asset ID
- Owner
- Ownership percentage

This simulates **fractional ownership**.

---

### 5️⃣ Transfer Token Ownership

Navigate to **Transfer Token**.

**Example Input:**
- Token ID:  
(Select a token)
- New Owner Name:  
`Ayesha Begum`

**What happens:**
- Ownership of the selected token is transferred
- A new block is added to the blockchain ledger
- Transfer history becomes immutable

---

### 6️⃣ Blockchain Ledger

Navigate to **Blockchain Ledger**.

**You will see:**
- Genesis block
- Asset registration blocks
- Tokenization blocks
- Transfer blocks
- Hash-linked chain ensuring immutability

---

## 🔐 Blockchain Principles Implemented

- Cryptographic hashing (SHA-256)
- Genesis block
- Hash chaining
- Immutable ledger
- Transaction-based record keeping

---

## 🎓 Academic Relevance

This project demonstrates:
- Blockchain fundamentals
- Asset tokenization
- Decentralized trust
- Practical implementation
- Real-world applicability

Suitable for:
- Project-based assessment
- Blockchain technology labs
- Final-year mini projects

---

## 🔮 Future Enhancements

- Blockchain validation (tamper detection)
- Role-based access control
- Smart contract simulation
- IPFS-based document storage
- Visual block explorer

---

## 📝 License

This project is developed for **educational purposes only**.

---

## 👨‍💻 Author

**Mohammed Zubair Uddin Zameer**  
Blockchain Technology – Academic Project
