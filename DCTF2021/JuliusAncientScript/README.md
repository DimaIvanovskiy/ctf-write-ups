# __DragonSec SI CTF 2021__ 
## _Julius' ancient script_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
CRYPTO | 100  | soska_nerealka

**Description:** 

> I found this Ancient Roman papyrus. Could you decypher it for me?
>
> flag.txt https://github.com/DimaIvanovskiy/ctf-write-ups/blob/main/DCTF2021/JuliusAncientScript/flag.txt

## Solution

Lets open flag.txt

```
rq7t{7vH_rFH_vI6_pHH1_qI67}
```


Task name and the description hints us that Caesar cipher was used for this text. So we should just find the correct shift.

We now that flag format is dctf{.+}.

So rq7t should be shifted to dctf. Firsly lets find difference between 'd' and 'r', and add it to every char in string.

```
a = 'rq7t{7vH_rFH_vI6_pHH1_qI67}'
shift = ord('d') - ord('r') # 14
res = ''
for i in a:
    res += chr(ord(i) + shift)
print(res) # dc)fm)h:Qd8:Qh;(Qb::#Qc;()o
```

The result is definitely no what we expected. but if we look at the begining of the flag it looks correct for 'd' 'c' and 'f' chars. But the third char should be 't'. So maybe its a modified Caesar cipher that has multiple shifts for every char category. '7' did not turn to 't' so maybe just all numbers have different shift. And also we can see that not numbers and not letters should be changed at all, like '{', '}' and '_'. Lets try to do it.

```
a = 'rq7t{7vH_rFH_vI6_pHH1_qI67}'
letter_shift = ord('d') - ord('r') # -14
digit_shift = ord('t') - ord('7') # 61
res = ''
for i in a:
    if i == "{" or i == "}" or i == "_":
        res += i
    elif i.isdigit():
        res += chr(ord(i) + digit_shift)
    else:
        res += chr(ord(i) + letter_shift)
print(res) #dctf{th:_d8:_h;s_b::n_c;st}
```

Again, not what we expected. But we can see that strange symbols appears in the result only on indexes where the input string contains upper letters. So we can tell that it also has different shift for such cases. If we look at the result we can creally tell that is this words 'b::n', 'th:' ':' char should be 'e' for normal sentence.

```
a = 'rq7t{7vH_rFH_vI6_pHH1_qI67}'
lower_letter_shift = ord('d') - ord('r') # -14
upper_letter_shift = ord('e') - ord('H') # -21
digit_shift = ord('t') - ord('7') # 61
res = ''
for i in a:
    if i == "{" or i == "}" or i == "_":
        res += i
    elif i.isdigit():
        res += chr(ord(i) + digit_shift)
    elif i.isupper():
        res += chr(ord(i) + upper_letter_shift)
    else:
        res += chr(ord(i) + lower_letter_shift)
print(res) #dctf{the_dce_hfs_been_cfst}
```

The result is wrong again. But that we remember that in flag its ok to use digits that represents symbols as in 1337 internet language.  And in this language 'e' is represented as '3'. 

```
a = 'rq7t{7vH_rFH_vI6_pHH1_qI67}'
lower_letter_shift = ord('d') - ord('r') # -14
upper_letter_shift = ord('3') - ord('H') # -21
digit_shift = ord('t') - ord('7') # 61
res = ''
for i in a:
    if i == "{" or i == "}" or i == "_":
        res += i
    elif i.isdigit():
        res += chr(ord(i) + digit_shift)
    elif i.isupper():
        res += chr(ord(i) + upper_letter_shift)
    else:
        res += chr(ord(i) + lower_letter_shift)
print(res) #dctf{th3_d13_h4s_b33n_c4st}
```


> dctf{th3_d13_h4s_b33n_c4st}
