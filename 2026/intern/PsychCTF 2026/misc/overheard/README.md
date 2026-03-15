# 『overheard』

no image this time :<

## 『The challenge』

![challs](/2026/intern/PsychCTF%202026/misc/overheard/image/challs.png)

## 『Highlight vulnerability and parts of interesting』

This challs is the classic one, buffer overflow

here are the script of the chall:
```c
#include <stdio.h>
#include <unistd.h>

void vuln() {
    char buf[64];
    write(1, "[WARD-COMM v1.3] Diagnostic mode active. Transmit message:\n", 59);
    read(0, buf, 1000);
}

int main() {
    vuln();
    return 0;
}
```

As you can see, there is limit on `buf` and the limit is 64. And this one is no pie if you take the look on image

## 『Solving Challenge』
> solved by Lylera

i tried to decompile online and it is exceed the time limit xD. So i use `pwndbg` to decompile and see of the memory. u can see this one:

[debug.txt](/2026/intern/PsychCTF%202026/misc/overheard/challs/debug.txt)

full of the stack memory :/ and yeah, you call the shell anyway. And there are no canary, just some function that trick us if there is "canary found". You can see this image:

![bof](/2026/intern/PsychCTF%202026/misc/overheard/image/bof.png)

Because of this, you can buffer overflow and then use the ropgadget. Because this is static linked, use this comment:

`ROPgadget --binary chall --ropchain`

and you will been given the shell payload automatic from ropgadget

The solper:

[solp.py](/2026/intern/PsychCTF%202026/misc/overheard/challs/solp.py)

![flag](/2026/intern/PsychCTF%202026/misc/overheard/image/flag.png)

## 『Flag』
```
psych{stat1c_1n_7h3_w4ll5}
```