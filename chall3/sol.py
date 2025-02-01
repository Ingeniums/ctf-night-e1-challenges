from Crypto.Cipher import AES

with open('challenge/output.txt','r') as f :
    ct = bytes.fromhex(f.readline().split(': ')[1])
pt = b''
for i in range(0,len(ct)-16,16) : 
    key = ct[i:i+16]
    cipher = AES.new(key,AES.MODE_ECB)
    pt += cipher.decrypt(ct[i+16:i+32])
print(pt)
 
