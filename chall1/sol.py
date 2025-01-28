from random import randint
from Crypto.Util.number import long_to_bytes
from math import gcd


with open('output.txt','r') as f :
    n1 = int(f.readline().split(': ')[1])
    c1 = int(f.readline().split(': ')[1])
    c2 = int(f.readline().split(': ')[1])
    eq = int(f.readline().split(': ')[1])




max = 1000
r = 0
for i in range(max) :
    d = gcd(n1,eq-i)
    if d!= 1 : 
        r = i
        break

eq_ = eq - r

E = eq_ // n1

n2 = eq_ - n1 * E

q = gcd(n1,n2)
p = n1 // q
z = n2 // q
d1 = pow(0x10001,-1,(p-1)*(q-1))
d2 = pow(0x10001,-1,(q-1)*(z-1))
m1 = pow(c1,d1,n1)
m2 = pow(c2,d2,n2)


print(long_to_bytes(m1)+long_to_bytes(m2))

