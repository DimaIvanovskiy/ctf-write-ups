# __HeroCTF_v3__ 
## _High Stakes_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Pwn | 50 | soska_nerealka

**Description:** 

> This casino is SOOOO totally rigged. I have lost everything .. I literally lost 300 times in a row ! This does not seem possible. I really wanted to buy the flag from the shop, but right now I'm so broke I'm not even allowed to think about it. Lucky as you are, you'll manage to win enough money to buy it for me, right bro ?
```
Host : pwn.heroctf.fr

Port : 9001
```

## Solution
First we connect
```
nc pwn.heroctf.fr 9001
```

Lets take a look at the casino.

This casino has fatal vulnerability: it does not take any money for placing the money.

Lets just put the bet on every number, win the money and buy the flag from the store.


> Hero{g4MBl1nG_f0R_dA_fL4G}
