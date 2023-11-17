#!/usr/bin/python3

import hashlib

def calculate_md5(filename):
    with open(filename, 'r') as file:
        text = file.read()
        # Calculate the MD5 hash of the modified text
        md5_hash = hashlib.md5(text.encode()).hexdigest()
        return md5_hash

permissions_filename = "evil-permissions.txt"

while True:
	calculated_md5 = calculate_md5(permissions_filename)
	print(f"Current MD5 Hash: {calculated_md5}")

	if calculated_md5.startswith("1842"):
	    print("Desired MD5 hash prefix found!")
	    break

	# Add spaces at the end of the file
	with open(permissions_filename, 'a') as file:
	    file.write(' ')  # You can adjust the number of spaces to add

