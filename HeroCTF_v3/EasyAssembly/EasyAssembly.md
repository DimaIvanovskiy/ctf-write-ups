# __HeroCTF_v3__ 
## _EasyAssembly_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Reverse | 40 | SoEasY

**Description:** 

> Don't worry, this one is quite easy :) Could be a good introduction to assembly !
>
> File: https://github.com/DimaIvanovskiy/ctf-write-ups/blob/main/HeroCTF_v3/EasyAssembly/EasyAssembly.asm

## Solution
Lets take a look at the main function:
```
main:
.LFB7:
        .cfi_startproc
        endbr64
        pushq   %rbp    #
        .cfi_def_cfa_offset 16
        .cfi_offset 6, -16
        movq    %rsp, %rbp      #,
        .cfi_def_cfa_register 6
        subq    $16, %rsp       #,
# EasyAssembly.c:17:    int input = getInput();
        call    getInput        #
        movl    %eax, -8(%rbp)  # tmp85, input
# EasyAssembly.c:19:    modified = input >> 2;
        movl    -8(%rbp), %eax  # input, tmp89
        sarl    $2, %eax        #, tmp88
        movl    %eax, -4(%rbp)  # tmp88, modified
# EasyAssembly.c:21:    if(modified == 1337404)
        cmpl    $1337404, -4(%rbp)      #, modified
        jne     .L5     #,
# EasyAssembly.c:22:            isGood = 0;
        movl    $0, isGood(%rip)        #, isGood
.L5:
# EasyAssembly.c:24:    if(!isGood)
        movl    isGood(%rip), %eax      # isGood, isGood.1_1
# EasyAssembly.c:24:    if(!isGood)
        testl   %eax, %eax      # isGood.1_1
        jne     .L6     #,
# EasyAssembly.c:25:            printf("Well done ! You can validate with the flag Hero{%d:%d}\n", input, modified);
        movl    -4(%rbp), %edx  # modified, tmp90
        movl    -8(%rbp), %eax  # input, tmp91
        movl    %eax, %esi      # tmp91,
        leaq    .LC1(%rip), %rdi        #,
        movl    $0, %eax        #,
        call    printf@PLT      #
        jmp     .L7     #
.L6:
# EasyAssembly.c:28:            puts("Argh... Try harder buddy you can do it !");
        leaq    .LC2(%rip), %rdi        #,
        call    puts@PLT        #
.L7:
# EasyAssembly.c:30:    return EXIT_SUCCESS;
        movl    $0, %eax        #, _11
# EasyAssembly.c:31: }
        leave
        .cfi_def_cfa 7, 8
        ret
        .cfi_endproc
```

As we can see the flag is "Hero{input:modified}".

IsGood must be 0 to print the flag. And we can see here:
```
# EasyAssembly.c:21:    if(modified == 1337404)
        cmpl    $1337404, -4(%rbp)      #, modified
        jne     .L5     #,
# EasyAssembly.c:22:            isGood = 0;
        movl    $0, isGood(%rip)        #, isGood
```
that isGood will be equal to 0 if modified == 1337404. So we found out modified.

Lets find input. 
```
        call    getInput        #
        movl    %eax, -8(%rbp)  # tmp85, input
# EasyAssembly.c:19:    modified = input >> 2;
        movl    -8(%rbp), %eax  # input, tmp89
        sarl    $2, %eax        #, tmp88
        movl    %eax, -4(%rbp)  # tmp88, modified
```
Here we see that we do "modified = input >> 2". So to get input we have to multiply modified by 4. input = 1337404 * 4 = 5349616


> Hero{5349616:1337404}
