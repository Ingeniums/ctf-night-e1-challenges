import hashlib
import os
'''MD5 hashing is considered outdated and insecure for cryptographic purposes, as it is vulnerable to collision attacks. 
It can still be used for non-security-critical tasks like file checksum verification, 
but it should not be relied upon for securing data or authentication '''
hashmd5_1={"username": "TEXTCOLLBYfGiJUETHQ4hEcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"}
hashmd5_2={"username": "TEXTCOLLBYfGiJUETHQ4hAcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"}
def find_passwords_with_matching_prefix(prefix_length=11, max_attempts=10**7):
    seen_hashes = {}

    for _ in range(max_attempts):
        # Generate a random password (you can adjust the length as needed)
        password = os.urandom(16).hex()  # 16 bytes = 32 hex characters

        # Compute the SHA-256 hash of the password
        hash_value = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Extract the first `prefix_length` hexadecimal characters of the hash
        hash_prefix = hash_value[:prefix_length]

        # Check if this prefix has been seen before
        if hash_prefix in seen_hashes:
            # If yes, return the two passwords and their hashes
            return {
                "password1": seen_hashes[hash_prefix],
                "password2": password,
                "hash_prefix": hash_prefix,
                "hash1": hashlib.sha256(seen_hashes[hash_prefix].encode('utf-8')).hexdigest(),
                "hash2": hash_value
            }
        else:
            # Otherwise, store the prefix and password
            seen_hashes[hash_prefix] = password

    # If no match is found within the max attempts
    return None


result = find_passwords_with_matching_prefix(prefix_length=11)

if result:
    print("Found two passwords with matching hash prefixes:")
    print(f"Password 1: {result['password1']}")
    hashmd5_1["password"]=result['password1']
    print(f"Password 2: {result['password2']}")
    hashmd5_2["password"]=result['password2']
    print(f"Matching Hash Prefix: {result['hash_prefix']}")
    print(f"Full Hash 1: {result['hash1']}")
    print(f"Full Hash 2: {result['hash2']}")
    print(hashmd5_1);
    print(hashmd5_2);
else:
    print("No matching passwords found within the maximum attempts.")
    
# output:
# {"username": "TEXTCOLLBYfGiJUETHQ4hEcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak", "password": "1682e1c479ec6de5968d986c08e18f90"}
# {"username": "TEXTCOLLBYfGiJUETHQ4hAcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak", "password": "51ac594a20d4c1c09e6a82f11afd6367"}

