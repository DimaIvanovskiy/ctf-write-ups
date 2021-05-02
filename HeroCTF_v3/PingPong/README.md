# __HeroCTF_v3__ 
## _Ping Pong_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Prog | 45 | xanhacks

**Description:** 

> Could you get the flag?
> 
>File: https://github.com/DimaIvanovskiy/ctf-write-ups/blob/main/HeroCTF_v3/PingPong/output.txt

## Solution
Lets take a look at the file first. It consists only from PING and PONG words. It looks like binary file where PING represents 1 and PONG represents 2.

Lets write code wich will make it look like a binary string: https://github.com/DimaIvanovskiy/ctf-write-ups/blob/main/HeroCTF_v3/PingPong/solution.py

Then i just used a web-site for binary decoding: https://www.rapidtables.com/convert/number/binary-to-ascii.html

> Hero{p1n6_p0n6_15_fun}
