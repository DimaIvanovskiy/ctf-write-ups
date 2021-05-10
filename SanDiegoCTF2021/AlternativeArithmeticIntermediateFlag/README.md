# __San Diego CTF 2021__ 
## _Alternative Arithmetic (Intermediate Flag)_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
MISC | 267 | soska_nerealka

**Description:** 

> Java has provided an alternative mathematical system. Please submit only the intermediate flag for this challenge.
>
> Connect via:nc java.sdc.tf 1337

## Solution
To solve this task we should answer the quiz:
```
Welcome to the 1337 Java quiz!
Make sure you learn its quirks before you start this journey.
Answer all questions to the best of your ability. Do not input any semicolons.
Good luck!
```
#### The first question.
```
1. Find a nonzero `long x` such that `x == -x`, enter numbers only, no semicolons:
```
This one is easy. The answer is Long.MIN_VALUE or -9223372036854775808.

Why? Well Long.MIN_VALUE = -2^(63) and Long.MAX_VALUE is 2^(63) - 1. So wen you do -Long.MIN_VALUE ot overflows and becomes Long.MIN_VALUE aagain. It is equal to Long.MAX_VALUE + 1


#### The second question.
```
Find 2 different `long` variables `x` and `y`, differing by at most 10, such that `Long.hashCode(x) == Long.hashCode(y)`
```
For this question we should look how long hash function works in java

![Javas long hash function](https://github.com/DimaIvanovskiy/ctf-write-ups/blob/main/SanDiegoCTF2021/AlternativeArithmeticIntermediateFlag/hash.jpg)

As we can see it is just xor of first half of the long number and the second one.
So lets take 0 and -1.

0 is 0000...0000 and its hash is 0. Nothing interesting.
But -1 is 111...111111...111. So its hash is 
111...111111...111
xor 
000...000111...111
(cast to int or just taking last half) =
000...000

Also 0

The naswer is 0 and -1.

#### The third question.
```
3. Enter a `float` value `f` that makes the following function return true:
boolean isLucky(float magic) {
    int iter = 0;
    for (float start = magic; start < (magic + 256); start++) {
        if ((iter++) > 2048) {
            return true;
        }
	}
	return false;
}
```

This task is about rounding of big float numbers. Float numbers does not contain all big numbers. And for some number x x+1=x, because next closest float number is too far and it will round up again to this number. 
But if we add 256 it can roundup to next float value. It is only left to find thin number. It cant be aeasily done by binary search made by hands.

The first answer I found was 2.41E9f.


> sdctf{JAVA_Ar1thm3tIc_15_WEirD}
