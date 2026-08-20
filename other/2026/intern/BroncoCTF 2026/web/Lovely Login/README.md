# 『Lovely Login』

![Challs](./assets/login.png)

# 『The challenge』

![challs](./assets/challs.png)

This is challs blind, again. So let solve it

# 『Highlight vulnerability and parts of interesting』

Because this is blind, lets test first 

![testing](./assets/try.png)

# 『Solving Challenge』
> solve by Lylera

Perhaps nothing show anything. So, lets do some crawling: robots.txt

![robots](./assets/clue_1.png)

There is b64 encode and some path to `/security`

![work](./assets/clue_2.png)

Well there is clue. The password is reverse of the word. For example if i type: `Yui`, we try to reverse it from that word it goes like this: `iuy`. Here are the result of decode:

![decode](./assets/decode.png)

After knowing this one, we can admin login with the pw: nimda

![flag](./assets/flag.png)

# 『Flag』

```
bronco{R3v3rs1ng_1s_S3cure}
```

## 『Source code』

- [index.html](./source_code/index.html)
- [robots.txt](./source_code/robots.txt)
- [security.html](./source_code/security.html)