# __HeroCTF_v3__ 
## _0xSSRF_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 60 | soska_nerealka

**Description:** 

> Get the flag !
URL : http://chall1.heroctf.fr:3000

## Solution
Lets look at this page. It contains http://chall1.heroctf.fr:3000/flag but you can enter it only from localhost.

This site is used for proxy, so we can use it to get the flag from localhost, but wen you try to use http://localhost:3000/flag we get the message "Are you trying to hack me?".

So we should use ssrf attakc(as the name of the task says).

I found realy good page about all variants of  ssrf: 

https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Request%20Forgery/README.md

I tried different variants but not all of them works because url shpuld be shorter than some length.

The only working url is http://0:3000/flag



Hero{cl4ssic_SSRF_byP4pass_251094}
