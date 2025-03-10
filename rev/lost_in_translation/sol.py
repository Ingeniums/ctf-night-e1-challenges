# The extracted encoded flag
encoded_flag = [
    0x43, 0x5D, 0x11, 0x00, 0x1C, 0x42, 0x46, 0x32, 
    0x58, 0x48, 0x43, 0x6C, 0x1E, 0x07, 0x04, 0x40, 
    0x6C, 0x31, 0x5D, 0x6C, 0x43, 0x57, 0x45, 0x07, 
    0x2D, 0x04, 0x5B, 0x6B, 0x19, 0x6C, 0x43, 0x5E, 
    0x29, 0x57, 0x42, 0x1A, 0x5D, 0x66, 0x10
]

# The XOR key
key = "r3v3rs3_m3"

# Decode the flag
flag = "".join(chr(encoded_flag[i] ^ ord(key[i % len(key)])) for i in range(len(encoded_flag)))

print(f"Recovered Flag: {flag}")
