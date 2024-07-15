```markdown
# Self-Signed UEFI Keys Generator

## Overview
This project allows users to generate and configure their own Platform Key (PK), Key Exchange Key (KEK), and Signature Database (db) keys for UEFI Secure Boot. The script will prompt for necessary information to create and self-sign these keys, which can then be imported into the kernel.

## Features
- Generates PK, KEK, and db keys.
- Prompts for user input to customize key parameters.
- Saves all keys and configuration files in a designated directory.
- Additional key management functionality to relocate and encrypt keys.

## Requirements
- Python 3.x
- `openssl` installed on your system
- `cryptography` library (install with `pip install cryptography`)

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/LionsLair1031/SelfSignedKeys.git
   ```

2. Navigate to the directory:
   ```bash
   cd SelfSignedKeys
   ```

3. Run the main script to generate keys:
   ```bash
   python3 __main__.py
   ```

4. After generating the keys, run the key manager to relocate and encrypt the keys:
   ```bash
   python3 key_manager.py
   ```

## Key Storage
The generated keys are initially saved in the `SelfSignedKeys` directory located in your Documents folder:
- **PK Key**: `~/Documents/SelfSignedKeys/PK.key`
- **KEK Key**: `~/Documents/SelfSignedKeys/KEK.key`
- **db Key**: `~/Documents/SelfSignedKeys/db.key`

After running the key manager, the keys will be securely stored in the user-specified directory.

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
   - Use the generated key files (`PK.key`, `KEK.key`, `db.key`) from the secure storage location.

6. **Save Changes and Exit**:
   - After enrolling the keys, save your changes before exiting the UEFI setup.

7. **Re-enable Secure Boot**:
   - If you disabled Secure Boot, re-enable it.

8. **Boot into Your Operating System**:
   - If configured correctly, your system should boot normally with the new keys.

## Author
- [LionsLair1031](https://github.com/LionsLair1031)
```

### Summary of Changes
- Added instructions for the new `key_manager.py` script.
- Clarified the key storage process after running the key manager.

Feel free to adjust any wording or details as needed! If you have further questions or requests, just let me know!
