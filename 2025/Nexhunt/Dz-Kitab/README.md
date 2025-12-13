# 『Dz-Kitab』

<img width="998" height="536" alt="image" src="https://github.com/user-attachments/assets/ef494dda-5310-4e3d-af6c-c2b9153288b3" />

# 『Challenge Overview』

This challenge is blind. Here are the source code:

- [index.html]()
- [book?id=2]()
- [book?id=3]()
- [book?id=4]()

I got this source code using `inspect`

# 『Solving challenge』
> Solved by: Lyra

This is kinda of idor if you might think because we given the id of book. if we go to `/book?id=2` it will show like this:

<img width="784" height="189" alt="image" src="https://github.com/user-attachments/assets/9ef9f2d5-2465-43be-9201-c24b793be645" />

# 『The issue』

If you go to `/book?id=1` it will show like this:

<img width="592" height="170" alt="image" src="https://github.com/user-attachments/assets/86cac02b-c68c-4530-ac64-ec890bb6b1f0" />

You must use the other way to get this things and getting the content of id=1. welp, you might think there is no way right since `id=1` get blocked that can't direct access it.

However, you can bypass this using http parameter pollution (hpp) like this: `/book?id=2&id=1`. So it will redirect to the last one since this running on express (i assume this is node js)

But the result like this:

<img width="657" height="213" alt="Screenshot 2025-12-13 174314" src="https://github.com/user-attachments/assets/bce0f4e3-4dd5-4041-861e-a97f4d40df22" />

# 『Solution』

The answer is on this website [node.js](https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html). As you can see, you use `[ ]` this one to http parameter pollution

So by giving this knowledge, i found 2 ways to bypass this one:

1. Burp suit -> send to repeater -> `/book?id=2&id=1` and some of http smuggle like this:

<img width="1490" height="415" alt="image" src="https://github.com/user-attachments/assets/3ff5b537-6548-4188-a724-201701e5e666" />

2. You can use this one instead: `/book?id[0]=2&id[1][]=1`:

<img width="759" height="329" alt="image" src="https://github.com/user-attachments/assets/5daf322d-2a44-4f2e-a7c7-fd4fb4ee69be" />

# 『Flag Format』
```
nexus{f4t_g3t++http_p4r4m3t3r_p0lut10n}
```
