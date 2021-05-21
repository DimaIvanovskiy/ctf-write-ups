# __DragonSec SI CTF 2021__ 
## _Very secure website_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
WEB | 200  | soska_nerealka

**Description:** 

> Some students have built their most secure website ever. Can you spot their mistake?
>
> http://dctf1-chall-very-secure-site.westeurope.azurecontainer.io/

## Solution

This website contains ling to its source file.

```
<?php
    if (isset($_GET['username']) and isset($_GET['password'])) {
        if (hash("tiger128,4", $_GET['username']) != "51c3f5f5d8a8830bc5d8b7ebcb5717df") {
            echo "Invalid username";
        }
        else if (hash("tiger128,4", $_GET['password']) == "0e132798983807237937411964085731") {
            $flag = fopen("flag.txt", "r") or die("Cannot open file");
            echo fread($flag, filesize("flag.txt"));
            fclose($flag);
        }
        else {
            echo "Try harder";
        }
    }
    else {
        echo "Invalid parameters";
    }
?>
```

This website uses tiger128,4  hash for username and password. Lets try crack '51c3f5f5d8a8830bc5d8b7ebcb5717df' hash using some online tools that contains base of all commonly used strings ands its hashes. Like https://md5hashing.net/hash/tiger128,4. 

We cracked username and it is 'admin'. :)

Ok, but we cant crack password so easily. What should we do? This website is written in php, but it uses '==' instead of '===' for string equality checking. Can we use it even if both of our compared variables has the same type(string)? It turns out that yes, we can. Php in '==' equality comparing tries to convert both of strings to number if they start with '0e', and it converts them to 0. Our second string starts with '0e'. So the only thing left is to find string which hash starts with '0e'.

I found page that contains string which start with '0e' for every commonly used hash, even for ours tiger 128,4. https://github.com/spaze/hashes

username: admin

password: LnFwjYqB


> dctf{It's_magic._I_ain't_gotta_explain_shit.}
