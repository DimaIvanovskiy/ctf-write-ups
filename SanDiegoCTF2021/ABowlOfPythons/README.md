# __San Diego CTF 2021__ 
## _A Bowl of Pythons_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
REVENGE | 136  | soska_nerealka

**Description:** 

> A bowl of spaghetti is nice. What about a bowl of pythons?
>
>chal.py: https://space.sdc.tf/

## Solution

Lets take a look at this python file and lets start a real revers engeneering hard work!
```
if __name__ == "__main__":
    e(b't2q}*\x7f&n[5V\xb42a\x7f3\xac\x87\xe6\xb4')
```
Input text hash should be equal to b't2q}*\x7f&n[5V\xb42a\x7f3\xac\x87\xe6\xb4'
```
h("Welcome to SDCTF's the first Reverse Engineering challenge.")
c = input("Input the correct flag: ")
if c[:6].encode().hex() != '{2}3{0}{1}{0}3{2}{1}{0}{0}{2}b'.format(*map(str, [6, 4, 7])):
	d()
if c[int(chr(45) + chr(49))] != chr(125):
	d()
```
"{2}3{0}{1}{0}3{2}{1}{0}{0}{2}b'.format(*map(str, [6, 4, 7]))" equals to "73646374667b". And if we find whitch text equals to this hex it is "sdctf{"

chr(45) == "-1" and chr(49)== - "1" and chr(125) == "}". Se it equals to "c[-1] != "}"

It is just a simple check that our input starts with "sdctf{" and ends with "}" (like every normal flag in this contest).

```
g = c[6:-1].encode()
if bytes( (g[i] ^ (a(i) & 0xff) for i in range(len(g))) ) != f:
	d()
h(b('4e696365206a6f622e20596f7520676f742074686520636f727265637420666c616721'))
```
We should find g

It can be easily done by this code
```
a = lambda n: a(n-2) + a(n-1) if n >= 2 else (2 if n == 0 else 1)

d = b't2q}*\x7f&n[5V\xb42a\x7f3\xac\x87\xe6\xb4'
y = [a(i) & 0xff for i in range(len(d))]
z = bytes([y[i] ^ d[i] for i in range(len(d))])
print(z)
```


> sdctf{v3ry-t4sty-sph4g3tt1}
