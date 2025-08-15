# 🔐 Local Password Manager

A secure, offline password manager built in **Python** that stores your credentials in an **encrypted** format using the `cryptography` library.  
This project ensures your data never leaves your device, providing full privacy and control.

---

## 📌 Features

- **Master Password Protection** – Access is locked with a master password (stored as SHA-256 hash).
- **AES Encryption** – All saved passwords are encrypted with Fernet symmetric encryption.
- **Add & View Credentials** – Save website, username, and encrypted passwords, and decrypt when needed.
- **Offline Storage** – No internet required; all data is stored locally in JSON files.
- **Multiple Attempts Security** – App locks after 3 incorrect master password attempts.

---

## 🛠️ Requirements

- Python 3.8+
- Install dependencies:
```bash
pip install cryptography
## project structure
local_password_manager/
│
├── main.py          # Main application script
├── key.key          # Encryption key (auto-generated on first run)
├── master.json      # Stores hashed master password
├── data.json        # Stores encrypted credentials
## 🚀 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/local_password_manager.git
cd local_password_manager


### 2️⃣ Install dependencies
```bash
pip install cryptography


### 3️⃣ Run the application
```bash
python main.py
## 📖 Usage

### **First Run**
- Generates an encryption key (`key.key`)
- Prompts you to create a master password
- Creates `master.json` to store the hashed password

### **Options**
1. **Add New Password** – Enter website, username, and password; it will be encrypted and saved.  
2. **View Saved Passwords** – Decrypts and displays stored credentials.  
3. **Exit** – Close the program.

---

## 🔐 Security Notes

- ❌ Do not share your `key.key` and `master.json` files.  
- ⚠ If `key.key` is lost, your saved passwords **cannot** be recovered.  
- 🔒 All encryption is done locally; no cloud storage is used.

---

## 🧑‍💻 Author

**Shahnwaz Akhtar**  
📧 Email: your-email@example.com  
🌐 GitHub: [yourusername](https://github.com/yourusername)

