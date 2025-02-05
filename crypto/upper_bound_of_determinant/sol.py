from Crypto.Cipher import AES
import random
n = 3
B = 50

with open('files/output.txt','r') as f :
    ct = f.readline().split(': ')[1]

max = round(pow(B,n) * pow(n,n/2))

for i in range(max) : 
    random.seed(i)
    key = random.randbytes(16)
    cipher = AES.new(key,AES.MODE_ECB)
    m = cipher.decrypt(bytes.fromhex(ct))
    if b'1ng3n1um5' in m :
        print(m)
        break
