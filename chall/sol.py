BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64_to_bits(b64_string):
    bits = ''.join(format(BASE64_CHARS.index(char), '06b') for char in b64_string if char in BASE64_CHARS)
    return bits

with open('challenge/output.txt', 'r') as f:
    base64_strings = f.readlines()

total_unhidden = ''
total_hidden = ''

for s in base64_strings:
    bits =  base64_to_bits(s)
    unhidden = bits[:(len(bits)//8) * 8]
    hidden = bits[len(unhidden):]
    total_unhidden += unhidden
    total_hidden += hidden


decoded_bytes = bytes([int(total_hidden[i:i+8], 2) for i in range(0, len(total_hidden), 8)])
print("Hidden Message:", decoded_bytes)
