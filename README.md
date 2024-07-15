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
https://github.com/LionsLair1031/SelfSignedKeys.git

2. Navigate to the directory:
cd SelfSignedKeys

3. Run the script:
python3 generate_keys.py


## Author
- [LionsLair1031](https://github.com/LionsLair1031)




Steps to Enroll Keys in UEFI Secure Boot
Prepare the Environment:

Ensure your system is configured to allow key enrollment. You might need to disable Secure Boot temporarily to make changes.
Access UEFI Firmware Settings:

Restart your computer and enter the UEFI/BIOS setup. This is usually done by pressing a key like F2, Delete, or Esc during boot (check your motherboard manual for specifics).
Navigate to Secure Boot Settings:

Look for a menu option related to "Secure Boot." This may be under "Boot," "Security," or "Authentication."
Enroll the Keys:

Find the option to manage or enroll keys.
There should be options to add a new Platform Key (PK), Key Exchange Key (KEK), and Signature Database (db).
Use the files you generated (e.g., PK.key, KEK.key, db.key).
Import the Keys:

Select the option to import each of the keys.
You may need to specify the path to the keys. If you generated them in the SelfSignedKeys directory, you might need to use a USB drive to transfer the files, as UEFI may not access them directly from the operating system.
Save Changes and Exit:

After enrolling the keys, ensure to save your changes before exiting the UEFI setup.
Re-enable Secure Boot:

If you had to disable Secure Boot to enroll the keys, re-enable it.
Boot into Your Operating System:

After saving and exiting, boot into your operating system. If everything is configured correctly, your system should boot normally with the new keys.
Verification
To verify that the keys were enrolled successfully:

You can check within the UEFI settings to see if your keys are listed.
If you encounter issues booting, you may need to troubleshoot or revert to default keys.
Important Notes
Make sure you have backups of your keys and configuration in case you need to restore the system.
Handle your keys securely to avoid security risks.
