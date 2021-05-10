# __San Diego CTF 2021__ 
## _A Prime Hash Candidate_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
CRYPTO | 157  | soska_nerealka

**Description:** 

> We hired a fresh MATH 187A student to create our login for us. After 6 months of backbreaking development, we're no longer storing passwords as plain text. Just try to break in!
>
> Hash function: https://github.com/DimaIvanovskiy/ctf-write-ups/blob/main/SanDiegoCTF2021/APrimeHashCandidate/server.py
>
> Connect via: nc phc1.sdc.tf 1337

## Solution

 Here is the servers code. We has hash of the password and we should find string with such hash. But it is not that easy because of the small prime number: 31. We cant just take PASSWD % 31 and say thaе chr(PASSWD % 31) is the last symbol of the password.

```
PASSWD = "59784015375233083673486266"


def find_hash(data):
    out = 0
    for c in data:
        out *= 31
        out += ord(c)
    return str(out)
```
 But we know that each "normal" symbol has ascii number somewhere between 32 and 126. So the last symbol in hash is x * 31 + PASSWD % 31 where x is from 1 to 4. 
 
Lets just brute force all remainders using this code:
```
from nclib import netcat

PASSWD = "59784015375233083673486266"


def find_hash(data):
    out = 0
    for c in data:
        out *= 31
        out += ord(c)
    return str(out)


def send_answer(symbols):
    conn = netcat.Netcat(('phc1.sdc.tf', 1337))
    print(conn.recvline())
    password = ''.join(list(map(chr, symbols))).encode()
    conn.sendline(password)
    print(conn.recvline())
    print(conn.recvline())


def find_password(hash, symbols):
    if hash == 0:
        print(''.join(list(map(chr, symbols))))
        send_answer(symbols)
        return symbols
    if hash < 0:
        return None
    a = hash % 31
    for i in range(1, 5):
        new_symbols = symbols.copy()
        new_hash = (hash - a - i * 31) // 31
        symbol = i * 31 + a

        new_symbols.insert(0, symbol)
        new_symbols = find_password(new_hash, new_symbols)
        if new_symbols is not None:
            return new_symbols
    return None


find_password(int(PASSWD), [])
```
The first password that this code finds is "Q#55914'"*#5*+0')"

> sdctf{st1ll_3553nt14lly_pl@1n_txt}
