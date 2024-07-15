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

