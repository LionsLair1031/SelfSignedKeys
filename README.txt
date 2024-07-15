```markdown
# Self-Signed UEFI Keys Generator

## Overview
This project allows users to generate and configure their own Platform Key (PK), Key Exchange Key (KEK), and Signature Database (db) keys for UEFI Secure Boot. The script will prompt for necessary information to create and self-sign these keys, which can then be imported into the kernel.

## Features
- Generates PK, KEK, and db keys.
- Prompts for user input to customize key parameters.
- Saves all keys and configuration files in a designated directory.
- Easy to use and modify.

## Requirements
- Python 3.x
- `openssl` installed on your system

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/LionsLair1031/SelfSignedKeys.git
   ```

2. Navigate to the directory:
   ```bash
   cd SelfSignedKeys
   ```

3. Run the script:
   ```bash
   python3 __main__.py
   ```

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
```

### Changes Made
- Added backticks for code blocks to improve formatting.
- Added periods for consistency in bullet points.
- Ensured clear separation of commands and instructions.

Feel free to use this version directly! If you need any more help or further adjustments, just let me know!
