# 『flag PDF』
> buka bang

author: hyall

<img width="564" height="472" alt="image" src="https://github.com/user-attachments/assets/04ff86df-21e6-47c0-852a-9eb52983750b" />


# 『The challenge』

We were given `Laporan_protected.pdf`. Here the result:

<img width="1919" height="1022" alt="image" src="https://github.com/user-attachments/assets/7e29b321-b2d2-477c-b30c-14d238738223" />

So lets solve this one.

# 『Solving challenge』
> solve by: Lylera_

So this is pdf lock. I suspicious something with this pdf for a while. Then i try to open it using strings to check it, here the result:

<img width="1919" height="625" alt="image" src="https://github.com/user-attachments/assets/aa87a470-498f-4e0b-b013-ca2595d49ef0" />

So this is weird, why there is `JS` inside this pdf metadata. i wonder what it could be, but if we open we need the password. So one of the solution is using `pdfcrack`. Here is [pdfcrack](https://pdfcrack.sourceforge.net/)

So lets crack this password to check what will happen of this `JS` function. here the result (command: `pdfcrack -f Laporan_protected.pdf -w /path/to/rockyou.txt`):

<img width="783" height="247" alt="image" src="https://github.com/user-attachments/assets/04f42ebb-fb24-48f6-bb11-ef091dc3892f" />

So we got the password, lets open it and copy it to open the password. Here the result if i strings that `JS` function:

<img width="1443" height="274" alt="image" src="https://github.com/user-attachments/assets/ddb45dd1-877c-450c-a016-a60ae2409d49" />

So now we can get clearly this mean of js function. Hemm...

# 『Flag』

So far this is more interesting. But wait, the challenge not over! I ask my friend on my team to solve this one but none of them can solve. But today, i suddenly solve this and using ai to make decrypt code of js. Here the command:

```
python3 - <<'PY'
nums = "0x63,0x6f,0x6d,0x70,0x69,0x74,0x7b,0x6d,0x61,0x6c,0x6c,0x31,0x63,0x31,0x6f,0x75,0x73,0x5f,0x70,0x64,0x66,0x5f,0x69,0x73,0x5f,0x63,0x72,0x34,0x7a,0x79,0x5f,0x30,0x61,0x33,0x64,0x62,0x35,0x32,0x37,0x32,0x31,0x30,0x39,0x32,0x30,0x66,0x39,0x32,0x37,0x64,0x65,0x37,0x33,0x37,0x31,0x65,0x63,0x66,0x31,0x38,0x33,0x66,0x33,0x7d"
print(''.join(chr(int(x,0)) for x in nums.split(',')))
PY
```

And here the result:

<img width="1447" height="146" alt="image" src="https://github.com/user-attachments/assets/d827bd02-a223-4cd8-9e5c-f59332fdcb87" />

```
Flag: compit{mall1c1ous_pdf_is_cr4zy_0a3db527210920f927de7371ecf183f3}
```
