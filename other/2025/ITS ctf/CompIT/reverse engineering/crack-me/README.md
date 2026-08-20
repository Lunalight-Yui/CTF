# 『crack-me』
> just crack it bro

Author: requiiem

# 『The challenge』

We were given `.me` file. Here the screenshot:

<img width="496" height="415" alt="image" src="https://github.com/user-attachments/assets/43a9cdc1-fcda-4ab4-b859-2f2ac68a0ff7" />

# 『Solving challenge』
> Solved by: Lylera_ but submit flag: leohack

To solve this one, we can use linux. Copy the file to folder of your linux. Then use `chmod +x crack.me`. Before use `./crack.me`, use `strings crack.me` first. Here the result:

<img width="321" height="188" alt="image" src="https://github.com/user-attachments/assets/f0a6fdbf-932e-424c-b357-5046d2547b84" />

As you can see, there is password and username. 

# 『Flag』

Then we can use `./crack.me` and input username and password:

```
Username: ristek
password: ctfcompit2025gaming!
```

here the result:

<img width="635" height="179" alt="image" src="https://github.com/user-attachments/assets/84dfe6c5-14c0-481b-b4c1-4442a3e76e11" />

```
Flag: compit{crackmes.one}
```
