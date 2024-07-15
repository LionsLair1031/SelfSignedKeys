import os
import subprocess

def sign_file(file_path, key_path, cert_path, output_path):
    """Sign a file using sbsign."""
    command = [
        'sbsign', 
        '--key', key_path, 
        '--cert', cert_path, 
        '--output', output_path, 
        file_path
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Signed: {file_path} -> {output_path}")
    except subprocess.CalledProcessError:
        print(f"Error signing file: {file_path}")

def main():
    # Paths to keys and certificates
    key_path = input("Enter path to your db.key: ")
    cert_path = input("Enter path to your db.cert: ")
    
    # Files to sign
    kernel_file = input("Enter path to the kernel file to sign: ")
    signed_kernel_file = f"{kernel_file}.signed"
    
    # Sign the kernel
    sign_file(kernel_file, key_path, cert_path, signed_kernel_file)

    # Sign additional binaries if needed
    while True:
        binary_file = input("Enter path to a binary to sign (or press Enter to finish): ")
        if not binary_file:
            break
        signed_binary_file = f"{binary_file}.signed"
        sign_file(binary_file, key_path, cert_path, signed_binary_file)

if __name__ == "__main__":
    main()

