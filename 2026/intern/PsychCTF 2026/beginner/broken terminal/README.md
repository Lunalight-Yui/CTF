# 『broken terminal』

no image :> because late to make it, bruh

# 『The challenge』

[challs](/2026/intern/PsychCTF%202026/beginner/broken%20terminal/challs/pwn_chal)

Download it.

# 『Highlight vulnerability and parts of interesting』

![ret2win](/2026/intern/PsychCTF%202026/beginner/broken%20terminal/image/vuln.png)

from the image, the vulnerability is the classic one: ret2win. This basically you can call the `win` function from the vulnerability.

we can expand the memory of vulnerable, here:

![bof](/2026/intern/PsychCTF%202026/beginner/broken%20terminal/image/bof.png)

this is bof ret2win challenge

As you can see, there is limit from the char `0x40` which mean the limit char: 64.


# 『Solving Challenge』
> solve by Lylera

There are 2 ways to solve this one:

the script one: [script](/2026/intern/PsychCTF%202026/beginner/broken%20terminal/challs/solver/script.py)

![script](/2026/intern/PsychCTF%202026/beginner/broken%20terminal/image/script.png)

or you can use `string` to see the challs xD:

![string_solve](/2026/intern/PsychCTF%202026/beginner/broken%20terminal/image/string_solve.png)

# 『Flag』
```
psych{0v3rfl0w_0p3n3d_th3_c3ll}
```