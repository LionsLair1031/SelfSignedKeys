```python
import os
import subprocess

# Create directory for keys
user_documents = os.path.expanduser("~/Documents")
keys_directory = os.path.join(user_documents, "SelfSignedKeys")

if not os.path.exists(keys_directory):
    os.makedirs(keys_directory)

# Function to prompt for user input
def prompt_user_info():
    print("Please provide the following information for the keys:")
    organization = input("Organization Name: ")
    name = input("Name: ")
    email = input("Email Address: ")
    location = input("Location (City, Country): ")
    
    return organization, name, email, location

# Function to generate keys and self-sign them
def generate_keys(organization, name, email, location):
    # Define key file paths
    pk_file = os.path.join(keys_directory, "PK.key")
    kek_file = os.path.join(keys_directory, "KEK.key")
    db_file = os.path.join(keys_directory, "db.key")

    # Generate PK key
    subprocess.run(["openssl", "req", "-new", "-x509", "-newkey", "rsa:2048", 
                    "-keyout", pk_file, "-out", pk_file, "-days", "3650",
                    "-nodes", "-subj", f"/CN={name}/O={organization}/emailAddress={email}/L={location}"])

    # Generate KEK key using the same details
    subprocess.run(["openssl", "req", "-new", "-x509", "-newkey", "rsa:2048", 
                    "-keyout", kek_file, "-out", kek_file, "-days", "3650",
                    "-nodes", "-subj", f"/CN={name}/O={organization}/emailAddress={email}/L={location}"])

    # Generate db key using the same details
    subprocess.run(["openssl", "req", "-new", "-x509", "-newkey", "rsa:2048", 
                    "-keyout", db_file, "-out", db_file, "-days", "3650",
                    "-nodes", "-subj", f"/CN={name}/O={organization}/emailAddress={email}/L={location}"])

    print("Keys generated successfully.")

# Main function to run the script
def main():
    organization, name, email, location = prompt_user_info()
    generate_keys(organization, name, email, location)

if __name__ == "__main__":
    main()
```

### Explanation

- **Directory Creation**: The script checks if the `SelfSignedKeys` directory exists in the user's Documents folder; if not, it creates it.
- **User Prompts**: It collects necessary information for generating the keys.
- **Key Generation**: Uses `openssl` to generate three self-signed keys (PK, KEK, and db) with the provided information.
- **Main Function**: This is the entry point of the script, orchestrating the prompt and key generation.

### Usage

1. Save this script as `key_generator.py`.
2. Run the script using Python:

   ```bash
   python3 key_generator.py
   ```

Let me know if you need any more modifications or additional features!
