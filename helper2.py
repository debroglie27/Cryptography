#!/usr/bin/python3

import hashlib

def calculate_md5(filename):
    with open(filename, 'r') as file:
        text = file.read()
        # Calculate the MD5 hash of the modified text
        md5_hash = hashlib.md5(text.encode()).hexdigest()
        return md5_hash

filename1 = "permissions1.txt"
filename2 = "permissions2.txt"

while True:
	# Add spaces at the end of the file
	with open(filename1, 'a') as file:
	    file.write(' ')
	    
	# Add spaces at the end of the file
	with open(filename2, 'a') as file:
	    file.write(' '*2)

	md5_1 = calculate_md5(filename1)
	md5_2 = calculate_md5(filename2)

	if md5_1[0:4] == md5_2[0:4]:
		print("Desired MD5 hash prefix found!")
		print(f"Permissions1 MD5 Hash: {md5_1}")
		print(f"Permissions2 MD5 Hash: {md5_2}")
		break

