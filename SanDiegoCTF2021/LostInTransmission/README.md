# __San Diego CTF 2021__ 
## _Lost in Transmission_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
CRYPTO | 96  | soska_nerealka

**Description:** 

> I had my friend send me the flag, but it seems a bit...off.
>
> Flag Message: https://github.com/DimaIvanovskiy/ctf-write-ups/blob/main/SanDiegoCTF2021/LostInTrasmission/flag.dat

## Solution

Lets take a look at this flag using some online HEX EDITOR like https://hexed.it/

We know that in this contest every flag starts with "sdctf", we should use this information and find out what transformation we should make with each hex number.

First symbol hex value is E6 or 230 in decimal system. And 's' symbol is 115. Second symbol hex value is C8 or 200 and 'd' symbol is 100.

It looks like we can just divide every symbol ascii number and we will get the correct answer.

Lest use this code:
```
with open('flag.dat', 'rb') as file:
    numbers = file.read()
    result = ''.join([chr(number//2) for number in numbers])
    print(result)
```


> sdctf{W0nD3rfUL_mY_G00d_s1R}
