from cryptography.fernet import Fernet
import os

def generate_key():
    """Generate and store a new key if it doesn't exist."""
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        print(" New encryption key generated.")
    else:
        print(" Encryption key already exists.")

# Run it
generate_key()

import hashlib
import json
from getpass import getpass

def create_master_password():
    """Creates and stores a hashed master password on first run."""
    if not os.path.exists("master.json"):
        print("\n First-time setup: Create your master password.")
        password = getpass("Enter new master password: ")
        confirm = getpass("Confirm master password: ")

        if password != confirm:
            print(" Passwords do not match. Try again.")
            return create_master_password()

        hashed = hashlib.sha256(password.encode()).hexdigest()

        with open("master.json", "w") as f:
            json.dump({"master": hashed}, f)
        
        print(" Master password created and saved securely.")
    else:
        print(" Master password already set.")

def verify_master_password():
    """Prompts user to unlock the app with their master password."""
    with open("master.json", "r") as f:
        stored = json.load(f)["master"]

    for attempt in range(3):
        password = getpass(" Enter master password: ")
        hashed = hashlib.sha256(password.encode()).hexdigest()

        if hashed == stored:
            print(" Access granted!")
            return True
        else:
            print(" Incorrect password. Try again.")
    
    print(" Too many failed attempts. Exiting.")
    exit()

    # main.py
from cryptography.fernet import Fernet
import os, json, hashlib
from getpass import getpass

def generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

def create_master_password():
    if not os.path.exists("master.json"):
        print("\n First-time setup: Create your master password.")
        password = getpass("Enter new master password: ")
        confirm = getpass("Confirm master password: ")

        if password != confirm:
            print(" Passwords do not match. Try again.")
            return create_master_password()

        hashed = hashlib.sha256(password.encode()).hexdigest()
        with open("master.json", "w") as f:
            json.dump({"master": hashed}, f)

        print(" Master password created.")
    else:
        print(" Master password already exists.")

def verify_master_password():
    with open("master.json", "r") as f:
        stored = json.load(f)["master"]

    for attempt in range(3):
        password = getpass("🔑 Enter master password: ")
        hashed = hashlib.sha256(password.encode()).hexdigest()

        if hashed == stored:
            print(" Access granted!")
            return True
        else:
            print(" Incorrect password.")
    
    print("🔒 Too many failed attempts.")
    exit()
    # Entry Point
generate_key()
create_master_password()
verify_master_password()
#storing encrypted password
import json
from cryptography.fernet import Fernet

def load_key():
    with open("key.key", "rb") as file:
        return file.read()

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    encrypted = encrypt_password(password)

    new_entry = {
        "website": website,
        "username": username,
        "password": encrypted
    }

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(new_entry)

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    print(" Password added successfully!")
    #for decryption (view saved password)
   
    def decrypt_password(encrypted_password):
        key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()
#view password function
    def decrypt_password(encrypted_password):
     key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()


def view_passwords():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(" No passwords found.")
        return

    if not data:
        print(" Password list is empty.")
        return

    print("\n Saved Passwords:\n")
    for entry in data:
        try:
            decrypted = decrypt_password(entry["password"])
            print(f" Website: {entry['website']}")
            print(f" Username: {entry['username']}")
            print(f" Password: {decrypted}")
            print("-" * 30)
        except Exception as e:
            print(f"⚠ Error decrypting: {e}")
           
            #replacing entry point
            # Entry Point
generate_key()
create_master_password()

if verify_master_password():
    while True:
        print("\nChoose an option:")
        print("1. Add a new password")
        print("2. View saved passwords")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

