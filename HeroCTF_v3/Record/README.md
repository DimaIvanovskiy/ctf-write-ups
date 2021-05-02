# __HeroCTF_v3__ 
## _Record_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 15 | soska_nerealka

**Description:** 

> Can you find anything special about this domain heroctf.fr ?

## Solution
Lets look at DNS records for the heroctf.fr. 
we can do it by "nslookup -type=txt heroctf.fr" command 
```
nslookup -type=txt heroctf.fr


╤хЁтхЁ:  UnKnown
Address:  192.168.1.1

Не заслуживающий доверия ответ:
heroctf.fr      text =

        "v=spf1 mx a -all"
heroctf.fr      text =

        "Hero{cl34rtXt_15_b4d}"
```
Here is our flag.


> Hero{cl34rtXt_15_b4d}
