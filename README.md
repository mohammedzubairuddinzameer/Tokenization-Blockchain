# 🔗 Blockchain-Based Tokenization of Real-World Assets

This project demonstrates how **real-world assets** such as property, gold, and certificates can be **digitally tokenized using blockchain principles**.  
It implements a **blockchain-like ledger**, enabling **fractional ownership, secure transfers, document verification, and user-based access control**.

The application is built using **Python and Streamlit** and uses **Supabase (PostgreSQL)** for persistent cloud storage.

---

## 🔍 Problem Statement

Traditional asset management systems:
- 📄 Rely on paper-based records  
- ⚠️ Are prone to fraud and manipulation  
- 🔒 Use centralized databases (single point of failure)  
- ⏳ Have slow ownership transfer processes  
- 🔗 Do not support fractional ownership  

---

## 🚀 Solution

This project solves the above issues using:

- 🔗 Blockchain-based transaction recording  
- 🔐 Cryptographic hashing (SHA-256)  
- 👥 Multi-user authentication system  
- 📦 Asset tokenization for fractional ownership  
- 🌐 Public / Private / Shared access control  
- 📁 Document hashing for tamper-proof verification  

---

## ✨ Features

- 👤 User Signup & Login (multi-user system)  
- 📦 Register real-world assets  
- 🔗 Tokenize assets into fractional ownership  
- 🔄 Transfer token ownership securely  
- 🔐 Upload documents → generate SHA-256 hash  
- ✅ Verify documents using hash comparison  
- 🌐 Asset visibility:
  - Private (owner only)  
  - Public (all users)  
  - Shared (specific users)  
- 📊 Blockchain ledger with hash chaining  
- ☁️ Persistent cloud storage using Supabase  

---

## 🛠️ Technology Stack

- **Python 3**
- **Streamlit (Frontend UI)**
- **Supabase (PostgreSQL Database)**
- **SHA-256 Cryptographic Hashing**
- **GitHub + Streamlit Cloud**

---

## 📁 Project Structure


tokenization-blockchain/
│
├── app.py # Main Streamlit application
├── asset_manager.py # Asset & token logic
├── blockchain.py # Blockchain implementation
├── auth.py # Authentication logic
├── db.py # Supabase connection
├── requirements.txt
├── README.md


---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository


git clone https://github.com/mohammedzubairuddinzameer/tokenization-blockchain.git

cd tokenization-blockchain


---

### 2️⃣ Install Dependencies


pip install -r requirements.txt


---

### 3️⃣ Configure Supabase

Create tables in Supabase:

#### users
- id (uuid)
- username
- password

#### assets
- id
- name
- owner
- value
- user_id
- visibility
- shared_with
- document_hash

#### tokens
- token_id
- asset_id
- owner
- percentage
- user_id

#### ledger
- id
- data
- previous_hash
- timestamp
- hash

👉 Disable Row Level Security (RLS) for all tables

---

### 4️⃣ Add Secrets (Streamlit)

Go to **Streamlit Cloud → Settings → Secrets**


SUPABASE_URL = "your_project_url"
SUPABASE_KEY = "your_anon_key"


---

### 5️⃣ Run Application


streamlit run app.py


Open:

http://localhost:8501


---

## 🧭 How to Use

### 🔹 1. Signup / Login
- Create account or login  
- Each user has isolated data  

---

### 🔹 2. Register Asset
Example:
- Name: Residential Plot – Hyderabad  
- Owner: Zubair  
- Value: 5000000  

Optional:
- Upload document → hash generated  

---

### 🔹 3. View Assets
- See assets based on visibility:
  - Private  
  - Public  
  - Shared  

---

### 🔹 4. Tokenize Asset
- Divide asset into tokens  
- Each token = fractional ownership  

---

### 🔹 5. Transfer Tokens
- Transfer ownership to another user  
- Blockchain records transaction  

---

### 🔹 6. Verify Document
- Upload same file → hash matches ✅  
- Modified file → mismatch ❌  

---

### 🔹 7. Blockchain Ledger
- View all transactions  
- Hash-linked chain ensures immutability  

---

## 🔐 Blockchain Concepts Used

- SHA-256 Hashing  
- Hash Linking  
- Immutable Ledger  
- Genesis Block  
- Transaction Recording  

---

## 📊 Example Workflow


User Login
↓
Register Asset
↓
Upload Document → Generate Hash
↓
Store in Database
↓
Create Blockchain Block
↓
Tokenize Asset
↓
Transfer Tokens


---

## 🎓 Academic Relevance

This project demonstrates:
- Blockchain fundamentals  
- Asset tokenization  
- Multi-user system design  
- Secure data handling  
- Real-world application of hashing  

---

## 🔮 Future Enhancements

- 🤖 Smart contracts integration  
- 🪙 Real blockchain network (Ethereum, etc.)  
- 📱 Mobile application  
- 🔐 Password hashing & MFA  
- 🌍 Government system integration  
- 📊 Analytics dashboard  
- ☁️ IPFS-based decentralized storage  

---

## 📝 License

This project is for **educational purposes only**.

---

## 👨‍💻 Author

**Mohammed Zubair Uddin Zameer**  
Blockchain Technology Project
