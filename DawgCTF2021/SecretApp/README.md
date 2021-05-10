# __DawgCTF 2021__ 
## _Secret App_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Reversing | 50 | soska_nerealka

**Description:** 

> I hid my flag in a secret app but I forgot what my username and password are.
>
> App: https://github.com/DimaIvanovskiy/ctf-write-ups/blob/main/DawgCTF2021/SecretApp/secret_app.exe

## Solution
Lets use IDA Freeware and disassamble secret_app.exe. 

Then we can open string subview and right there we find our username: not_username and password: not_password

![String subview in IDA](https://github.com/DimaIvanovskiy/ctf-write-ups/blob/main/DawgCTF2021/SecretApp/string_subview.png)



> Hero{H3yyyy_Th4t5_pr3tTy_gO0d}
