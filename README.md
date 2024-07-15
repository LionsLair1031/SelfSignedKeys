```markdown
# Self-Signed UEFI Keys Generator

## Overview
This project allows users to generate and configure their own Platform Key (PK), Key Exchange Key (KEK), and Signature Database (db) keys for UEFI Secure Boot. The script prompts for necessary information to create and self-sign these keys, which can then be imported into the kernel. This guide will help you navigate through the process of securing your operating system with UEFI Secure Boot.

## Features
- **Key Generation**: Generate PK, KEK, and db keys.
- **Key Management**: Relocate and encrypt keys for secure storage.
- **Key Signing**: Sign the kernel and binaries to ensure they are trusted.
- **Future Signing**: Easily sign additional binaries with a dedicated script.

## Requirements
- Python 3.x
- `openssl` installed on your system
- `cryptography` library (install with `pip install cryptography`)
- `sbsigntool` (install with `sudo apt install sbsigntool`)

## Usage

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/LionsLair1031/SelfSignedKeys.git
```

### Step 2: Navigate to the Directory
Change to the directory:
```bash
cd SelfSignedKeys
```

### Step 3: Generate Keys
Run the key generation script:
```bash
python3 __main__.py
```
Follow the prompts to generate your PK, KEK, and db keys.

### Step 4: Relocate and Encrypt Keys
After generating the keys, run the key management script to relocate and encrypt them:
```bash
python3 key_manager.py
```
You will be prompted to specify a secure storage location and create a password for encryption.

### Step 5: Sign the Kernel and Binaries
Run the key signing script to sign the kernel and any necessary binaries:
```bash
python3 key_signer.py
```
Follow the prompts to enter the paths for your keys and the files you want to sign. The signed files will have a `.signed` extension.

### Step 6: Enroll the Keys in UEFI Secure Boot
1. **Prepare the Environment**:
   - Ensure your system is configured to allow key enrollment. You might need to disable Secure Boot temporarily.

2. **Access UEFI Firmware Settings**:
   - Restart your computer and enter the UEFI/BIOS setup (usually by pressing `F2`, `Delete`, or `Esc` during boot).

3. **Navigate to Secure Boot Settings**:
   - Look for "Secure Boot" options under "Boot," "Security," or "Authentication."

4. **Enroll the Keys**:
   - Use the generated key files (`PK.key`, `KEK.key`, `db.key`) from the secure storage location.

5. **Save Changes and Exit**:
   - After enrolling the keys, save your changes before exiting the UEFI setup.

6. **Re-enable Secure Boot**:
   - If you disabled Secure Boot, re-enable it.

7. **Boot into Your Operating System**:
   - If configured correctly, your system should boot normally with the new keys.

## Future Binary Signing
To easily sign additional binaries in the future, run the key signing script again:
```bash
python3 key_signer.py
```
This allows you to quickly sign any new binaries that need to be added to your Secure Boot configuration.

## Author
- [LionsLair1031](https://github.com/LionsLair1031)

## Summary
This guide outlines the complete process from generating UEFI keys to signing and enrolling them, ensuring your operating system operates securely under UEFI Secure Boot. Follow each step to maintain a streamlined and efficient workflow.
```

### Key Updates
- **Structured Steps**: Clearly defined steps for each phase of the process.
- **Future Binary Signing**: Included details on how to sign additional binaries easily.
- **User-Friendly**: Simplified language and step-by-step instructions for clarity.

Feel free to adjust any sections or add additional details as needed! If you have more requests, just let me know!
