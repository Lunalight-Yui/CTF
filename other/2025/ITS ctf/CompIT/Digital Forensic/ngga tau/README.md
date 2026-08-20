# 『ngga tau』
> aku perlu ini

<img width="554" height="465" alt="image" src="https://github.com/user-attachments/assets/1628050d-f4a8-4e60-978f-d2178fda3f75" />

Author: hyall

# 『The challenge』

We were given png file. Here the result:

![chall (2)](https://github.com/user-attachments/assets/681b6456-0c22-426b-85f4-fc4fd2aefbda)

Seems nothing suspicious, but lets try to solve!

# 『Solving challenge』
> Solve by: Lylera_

One of my thought to solve this is using `strings`. Because, i wanna see these file what can make hidden inside of metadata. So here i try to strings this image:

<img width="305" height="649" alt="image" src="https://github.com/user-attachments/assets/4ca78df9-6fbf-4bfd-a5e0-a084880e9327" />

As i expected. so there is `flag.txt` file name. So i can find another way to check it by using [exiftool](https://exiftool.org/). click that to gain website of Exiftool.

So to execute my plan, i use this command `exiftool <filename>`. Here the result:

<img width="767" height="562" alt="image" src="https://github.com/user-attachments/assets/1b344370-2c34-4b0b-9dee-758d3d5779cd" />

So nothing found as i expected. well then, i use another way to get that by using `binwalk`. Click this one: [binwalk](https://www.kali.org/tools/binwalk/)

To extract any file inside `chall.png`, i use this command: `binwalk -e chall.png`. Here the result:

<img width="1477" height="358" alt="image" src="https://github.com/user-attachments/assets/87c1796b-b42e-476b-94c5-469a0dc9b9e4" />

As you can see. there are file name `_chall.png.extracted` which mean there is a file inside this image and we can get to extract it. After that, we can open this file and... 

<img width="1076" height="150" alt="image" src="https://github.com/user-attachments/assets/f0d33d43-d877-4781-9eb5-ce1b84d9f2a8" />

Seems this `flag.txt` has get lock. Hemmm, we can use `john the ripper` as same name as on image. What is john the ripper? click this: [john the ripper](https://www.openwall.com/john/).

So we can use this command step by step:

```
1. zip2john 1DF7B.zip > a.hash (to become hash first)
2. john --wordlist=/usr/share/wordlists/rockyou.txt 1DF7B.hash (bruteforcing the password)
3. john --show 1DF7B.hash (to show the password)
```

So lets try it. Here the result:

<img width="1464" height="507" alt="image" src="https://github.com/user-attachments/assets/8f5b5c16-d282-42cb-9e74-3b4792230562" />

# 『Flag』

After getting the password, we can unzip this file to get the flag.txt. Here the result (password: `Bandit101`) :

<img width="930" height="434" alt="image" src="https://github.com/user-attachments/assets/5c8fbaab-090c-4702-9b4d-e690af6fa052" />

```
Flag: compit{cb433a507d9b3bdcd1481550b38aaa474a15452897193d1cbec25277d763323f}
```
