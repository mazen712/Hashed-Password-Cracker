Hashed Password Cracker
------------------------

This script is a Hashed Password Cracker that allows you to crack passwords using different hashing algorithms (MD5, SHA-256, SHA-512) and with multi-threading.

Features:
- Supports MD5, SHA-256, and SHA-512 hashing algorithms.
- Allows multi-threading to speed up the password cracking process.
- Provides a progress indicator to show the percentage of passwords checked.
- Handles errors such as incorrect dictionary file paths and unsupported hashing algorithms.
- Measures the time taken to crack the password.

Usage:
1. Install Python (version 3.x) and the required libraries (`hashlib`, `threading`, `time`).
2. Run the script in a Python environment.
3. Enter the target hash, dictionary file path, hashing algorithm, and number of threads when prompted.
4. The script will start cracking the password and display the progress and the time taken.

Note: The dictionary file should contain one password per line. The script assumes that the dictionary file is in the same directory as the script or provide the full path to the dictionary file when prompted.

This script provides a basic framework for a Hashed Password Cracker and can be further enhanced with additional features and optimizations based on specific requirements.

Remember to keep the dictionary file in the same directory as the script or provide the full path to the dictionary file when prompted.
