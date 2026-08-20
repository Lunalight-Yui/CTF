# 『Web Daveloper』

<img width="994" height="530" alt="image" src="https://github.com/user-attachments/assets/e91c67c0-66ef-435e-a1eb-75f5d6a2ddf8" />

# 『Challenge Overview』

This challenge is blind meaning that there are no source code and must finding what kind of exploitation on this challenge

# 『Solving Challenge』
> Solved by daffainfo and then Lyra

Since this is new for me, i learn anything from this challenge. This challenge is kinda different from i know, meaning we must Web Daveloper Exploitation.

# 『The issue』

The first thing is i would never that i must do in here. Here are the result of main:

<img width="684" height="216" alt="image" src="https://github.com/user-attachments/assets/0153251d-35a0-4a28-bec2-c348816bc2a5" />

For this , i try use chat gpt and gemini to give me an explaination more about this since this is new. I also ask (now) for the documentation that i must read it.

# 『Solution』

After i found this documentation, i learn that we can use `PROPFIND` for finding something hidden inside this challenge. Logically, it will be same as `ls` if you try look on file in website.
The result:

<img width="1493" height="747" alt="image" src="https://github.com/user-attachments/assets/f8d7297d-489e-4f51-bde4-57ee26621452" />

Giving me this information about using another http method. i use `X-HTTP-Method-Override` for overriding `GET` method, the result:

<img width="1492" height="796" alt="image" src="https://github.com/user-attachments/assets/e76e0390-c876-46ab-93d2-ed9a0e0bd0f9" />

After finding this, it will much closed to the right path and give me a clue for this. I use another trick, that is `Depth: 1`. Here the result:

<img width="1520" height="831" alt="image" src="https://github.com/user-attachments/assets/55af626c-9a31-46ec-b05e-d441ea5d501d" />

Then i search for the flag.txt, and it is on the `/vault/flag.txt`. here the result:

<img width="1515" height="834" alt="image" src="https://github.com/user-attachments/assets/6b15428d-ae33-4c7f-86c8-861c59bf6692" />

Then if you try `/vault/flag.txt` while `X-HTTP-Method-Override` still on the header, it will see the property of website body and just `<file>flag.txt</file>`

You might think, well just delete `X-HTTP-Method-Override` command and you will get the flag. the problem is:

<img width="1142" height="325" alt="image" src="https://github.com/user-attachments/assets/d3134765-bf80-4504-a385-c38dae90fc9c" />

So yeah, use another tricks: `X-Original-URL: /vault/flag.txt` and you will get flag:

<img width="1137" height="335" alt="image" src="https://github.com/user-attachments/assets/d1ea8c53-ddee-4baf-8795-27c0dbd75ffd" />

# 『Flag Format』
```
nexus{w3bd4v_wchw3y4_h3d34rs_ezzzzzzzzz}
```
