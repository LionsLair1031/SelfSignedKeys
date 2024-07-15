import os
from cryptography.fernet import Fernet
import getpass

def create_secure_storage(storage_path):
    """Create a secure storage directory if it doesn't exist."""
    if not os.path.exists(storage_path):
        os.makedirs(storage_path)
        print(f"Secure storage created at: {storage_path}")
    else:
        print(f"Secure storage already exists at: {storage_path}")

def generate_key(password):
    """Generate a key from the provided password."""
    return Fernet(Fernet.generate_key())

def encrypt_file(file_path, password):
    """Encrypt a file using the provided password."""
    key = generate_key(password)
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted_data = key.encrypt(data)
    
    with open(file_path, 'wb') as f:
        f.write(encrypted_data)
    
    return key

def move_keys_to_secure_location(keys, storage_path, password):
    """Move and encrypt key files to a secure location."""
    for key_file in keys:
        # Encrypt the key file
        encrypt_file(key_file, password)
        # Move the key file
        os.rename(key_file, os.path.join(storage_path, os.path.basename(key_file)))
        print(f"Moved and encrypted {key_file} to {storage_path}")

def main():
    # Prompt for secure storage location
    storage_path = input("Enter secure storage directory: ")
    create_secure_storage(storage_path)
    
    # Prompt for password
    password = getpass.getpass("Enter a password for key encryption: ")

    # List of key files to move
    keys = ['PK.key', 'KEK.key', 'db.key']  # Adjust based on actual key file paths

    move_keys_to_secure_location(keys, storage_path, password)

if __name__ == "__main__":
    main()

