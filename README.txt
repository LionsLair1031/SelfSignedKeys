# Self-Signed UEFI Keys Generator

## Overview
This project allows users to generate and configure their own Platform Key (PK), Key Exchange Key (KEK), and Signature Database (db) keys for UEFI Secure Boot. The script will prompt for necessary information to create and self-sign these keys, and then import them into the kernel.

## Features
- Generates PK, KEK, and db keys
- Prompts for user input to customize key parameters
- Saves all keys and configuration files in a designated directory
- Easy to use and modify

## Requirements
- Python 3.x
- `openssl` installed on your system

## Usage
1. Clone this repository:
git clone https://github.com/LionsLair1031/SelfSignedKeys.git

css
2. Navigate to the directory:
cd SelfSignedKeys

markdown
3. Run the script:
python3 main.py

markdown
## Steps to Enroll Keys in UEFI Secure Boot
1. **Prepare the Environment**:
- Ensure your system is configured to allow key enrollment. You might need to disable Secure Boot temporarily to make changes.

2. **Access UEFI Firmware Settings**:
- Restart your computer and enter the UEFI/BIOS setup (usually by pressing `F2`, `Delete`, or `Esc` during boot).

3. **Navigate to Secure Boot Settings**:
- Look for "Secure Boot" options, typically found under "Boot," "Security," or "Authentication."

4. **Enroll the Keys**:
- Find the option to manage or enroll keys and select the option to add a new PK, KEK, and db.

5. **Import the Keys**:
- Use the generated key files (`PK.key`, `KEK.key`, `db.key`).
- You may need to transfer the files to a USB drive if UEFI doesn’t access them directly from the OS.

6. **Save Changes and Exit**:
- After enrolling the keys, save your changes before exiting the UEFI setup.

7. **Re-enable Secure Boot**:
- If you disabled Secure Boot, re-enable it.

8. **Boot into Your Operating System**:
- If configured correctly, your system should boot normally with the new keys.

## Author
- [LionsLair1031](https://github.com/LionsLair1031)
