from Crypto.Cipher import AES
from flag import flag
from os import urandom

key = urandom(16)

ct = b''
for i in range(0,16*4,16):
    cipher = AES.new(key,AES.MODE_ECB)
    ct += cipher.encrypt(flag[i:i+16])
    key = ct[i:i+16]

with open('output.txt','w') as f : 
    f.write(f'ct : {ct.hex()}')

