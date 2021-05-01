# __HeroCTF_v3__ 
## _PwnQL #1_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Misc | 50 | Enarior/xanhacks

**Description:** 

> Go deeper 
>
>File : https://github.com/DimaIvanovskiy/ctf-write-ups/blob/main/HeroCTF_v3/Russian_doll/archive.zip


## Solution
If we unzip this file we can notice that everey directory has its own subdirectory and its look like this directory-raw is infinite and we cant just get the root file by clicking.

So lets just use simple command "ls -R". It will show us all subdirectories. Than we should echo ...../flag.txt and get the flag.


> Hero{if_yOu_gOt_HEre_By_clIcKInG_mANnUaLly_YoU_sHOuLd_REalLy_SeE_SoMeOne}
