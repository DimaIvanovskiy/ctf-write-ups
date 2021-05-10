# __San Diego CTF 2021__ 
## _A Primed Hash Candidate_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
CRYPTO | 293 | soska_nerealka

**Description:** 

> After the rather embarrassing first attempt at securing our login, our student intern has drastically improved our security by adding more parameters. Good luck getting in now!
>
> Server: https://github.com/DimaIvanovskiy/ctf-write-ups/blob/main/SanDiegoCTF2021/APrimedHashCandidate/server.py
>
> Connect via: nc phc2.sdc.tf 1337

## Solution

Look at the server.py. It has one significant vulnerability: it returns to us computed hash if it is not equal to hash password. We can use it.
```
from nclib import netcat
import re
import math
PASSWD = 91918419847262345220747548257014204909656105967816548490107654667943676632784144361466466654437911844


conn = netcat.Netcat(('phc2.sdc.tf', 1337))
conn.recvline()

hashes = {}
for i in range(1, 7):
    conn.sendline(chr(i).encode())
    string_with_hash = conn.recvline()
    conn.recvline()
    new_hash = int(re.findall(b'\d+', string_with_hash)[0].decode())
    hashes[i] = new_hash
```
Here we just compute and save hashes for first 6 ascii symbols.

Then lets use this hashes to find secret3 and last secret2 symbol ascii number. 
We can just brute force last symbol of secret2 which is somewhere between 40 and 127 also we kno that secret 3 is three-digit.
(hash - lastSecret2Symbol) % secret3 should be equals to 0. So if it is no correct out lastSecret2Symbol and secret3 are incorrect. And i find all possible secret3 for all hashes and than just finf their intersection. It should be out secret3. In our case secret3 is 233.
```
resultSecret3 = 0
for last_secret2 in range(40, 127):
    for secret3 in range(100, 1000):
        possible_secret3 = {}
        for i in range(1, 7):
            new_hash = hashes[i] - last_secret2
            if new_hash % secret3 == 0:
                if i not in possible_secret3:
                    possible_secret3[i] = set()
                possible_secret3[i].add(secret3)
            else:
                break
        if len(possible_secret3.values()) !=6:
            continue
        result = None
        for i in range(1, 7):
            if (i == 1):
                result = possible_secret3[1]
            else:
                result = result & possible_secret3[i]
        if len(result)!= 0:
            resultSecret3 = secret3

secret3 = resultSecret3
```
Than we can easily find secret2 because we know that secret3 is quiet big and there will be no collisions because of small prime.
```
secret2= []
new_hash = hashes[1]
while new_hash != 0:
    a = new_hash % secret3
    secret2.insert(0, a)
    new_hash = (new_hash - a ) // secret3

secret2 = secret2[1:]
```
Only secret1 is left. We dont know the length of secret1 but lets use some big password so every symbol of secret1 is used. 
If password is too short only first symbols of secret1 will be used because of this code in server:
```
 data = [ord(x) ^ ord(y) for x,y in zip(data,secret1*len(data))]
```
We can easily find secret 1 because we know whar password is and what length of secret2 is. And we know that if x ^ y = z than x = z ^ y.
```
conn.sendline(b'111111111111111111111111111111111111111111111111111')
string_with_hash = conn.recvline()
conn.recvline()
new_hash = int(re.findall(b'\d+', string_with_hash)[0].decode())


secret1 = []
data = []
while new_hash != 0:
    a = new_hash % secret3
    data.insert(0, a)
    new_hash = (new_hash - a ) // secret3

data = data[:len(secret2) + 3]
for x in data:
    secret1.append(x ^ ord('1'))
```
Now we have all that we wanted. Lets find the password and send it to find flag.
```
data = []
new_hash = PASSWD
while new_hash != 0:
    a = new_hash % secret3
    data.insert(0, a)
    new_hash = (new_hash - a ) // secret3

res = []
data = data[:len(secret2)+3]
for i in range(len(data)):
    res.append(data[i] ^ secret1[i])

res = ''.join(list(map(chr, res))).encode()
conn.sendline(res)
conn.recvline()
print(conn.recvline())
```
Pssword is "GZZ9t3W3Ar34un44m8PLXX6"


> sdctf{W0W_s3cur1ty_d1d_dRaStIcAlLy_1mpr0v3}
