# __DragonSec SI CTF 2021__ 
## _Company leak_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
MISC | 500  | soska_nerealka

**Description:** 

> Someone hacked and leaked some very important data from an evil company. Find their dirty secrets and expose them!
>
> leaked.zip: https://github.com/DimaIvanovskiy/ctf-write-ups/blob/main/DCTF2021/CompanyLeak/leaked.zip

## Solution

Firstly, lets unzip leaked.zip. This zip has 2 files: README.md and super_secret.zip. We cant unzip second file because it has password on it, but we can see that it contains 2 files: README.md and top_secre.txt. Considering by sizes and text in README.md this files are the same.

That means that we can use plain text attack on this zip using bkcrack tool. https://github.com/kimci86/bkcrack

We should zip README.md that is known to us to README.zip and use bkcrack with this options:
```
bkcrack.exe -C super_secret.zip -p README.md -c README.md -P readme.zip
```

This will give us 3 keys 
```
a33fbdc6 5b49420e 6589766e
```

Then we again use bkcrack to change password for encrypted zip using this command:
```
bkcrack -C super_secret.zip -k a33fbdc6 5b49420e 6589766e -U not_super_secret.zip easy
```

Now we have zip file with known to us password. We can open it and find flag in top_secret.txt.


> dctf{wew_lad_y0u_aCtually_d1d_it}
