# __HeroCTF_v3__ 
## _PwnQL #1_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 50 | soska_nerealka

**Description:** 

> Login as admin to get the flag.
URL : http://chall1.heroctf.fr:8080

## Solution
We should look at the source code of the web page with the devtools. Here we can find comment right in the code. <!-- Hello dev, do not forget to remove login.php.bak before committing your code. -->

Lets dowload and take a look at this file. http://chall1.heroctf.fr:8080/login.php.bak
Here it is: https://github.com/DimaIvanovskiy/ctf-write-ups/blob/main/HeroCTF_v3/PwnQl1/login.php.bak

Here we can see that LIKE functions is used for password comparison. That means that we can just use % as a password, whitch matches any string.
Using this data we get our flag

username : admin

password : %


> Hero{pwnQL_b4sic_0ne_129835}
