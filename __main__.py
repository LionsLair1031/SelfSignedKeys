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
