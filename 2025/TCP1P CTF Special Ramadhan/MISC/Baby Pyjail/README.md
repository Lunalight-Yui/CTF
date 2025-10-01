# Baby Pyjail
> baby pyjail

> Start challenge from: https://ctfify.1pc.tf/challenge/misc_baby_pyjail

> [Zip File](https://tcp.1pc.tf/assets/c728938331c5495b03d78d3cf9cd71f039ff8fbe5812f2b96cc55ed91062e459/babypyjail_babypyjail-dist.zip)

Author: daffainfo

# Code Chall
```
inp = input("Input pls")

if any(c in inp for c in "abcdefghijklmnopqrstuvwxyz0123456789_\"'."):
    print("Invalid input!")
else:
    print(eval(inp))
```

# Solve
