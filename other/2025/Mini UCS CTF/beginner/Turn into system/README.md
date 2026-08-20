# Turn Into System
> The basic knowledge that you must be know is SSH, this service/program will let you turn into the server system, go and find the way how to connect with SSH service.

```
host     : minictf.ucs.or.id
port     : 1337
user     : ucs
password : UCSITS2025!!!
```
Author: rootkids

Solve:

SSH is a cryptographic network protocol that enables secure remote access to computers, particularly Linux servers, over an unsecured network like the internet. There are many command about ssh. If you want to know, 
you can learn on this website `https://linux.die.net/man/1/ssh`.

Back to topic. If you didn't know how it work, try to type this one (for example):

```
ssh <user>@<host> -p <port>
```

I try this `ssh ucs@minictf.ucs.or.id -p 1337`. The result:

<img width="485" height="60" alt="image" src="https://github.com/user-attachments/assets/b12ef714-ee24-4c38-9acb-e6ebf423c9a9" />

Once you entered the password (and the password is correct), the program should be like this:

<img width="751" height="490" alt="Screenshot 2025-09-06 101235" src="https://github.com/user-attachments/assets/dbc58080-fb89-485a-b98c-b9792735d53a" />

`Then now what should i do now`, right? there are many type of commands in linux. Try to use `ls`. If the result like this:

<img width="239" height="44" alt="image" src="https://github.com/user-attachments/assets/9a1e427a-ec76-4f78-b79d-3762796f4389" />

try to 
```
cd ..
```
It go to one way back from folder we reach to one step before. If you confused what i say, i use this logic: 

Take a look the example: 
```
C:/Downloads/Ly/What_do_you_want/Nothing_interest_here/get_out
```
If i use `cd ..`, it will become like this:
```
C:/Downloads/Ly/What_do_you_want/Nothing_interest_here
```
i hope you can understand for what i mean ^^ (and i will explain it on another file to explain about linux command like ls, cd, cat, and etc). Next, i use `cd ..` on this program and result:

<img width="364" height="83" alt="image" src="https://github.com/user-attachments/assets/e5b0e3f9-5faf-47e9-a307-b9c711ff5558" />

Then, we try again like same method `cd ..` and `ls` and the result became like this:

<img width="607" height="255" alt="image" src="https://github.com/user-attachments/assets/966f1a68-e024-4d9e-a5c3-41a732105f16" />

Next one, there is a file name `44e3a5417e3307caeb347abdf02b1915_flag.txt`. You can use this:
```
cat 44e3a5417e3307caeb347abdf02b1915_flag.txt
```
to see a information inside this file. and the result like this:

<img width="812" height="50" alt="image" src="https://github.com/user-attachments/assets/293a0a10-90cf-4207-a45a-6e4f6f79c4a0" />

```
flag: UCS{SSH_IS_th3_1mport4nt_c0mmand_program_th4t_You_should_kn0w!!!!}
```
