# 『execute-me』
> just run it bro

Author: requiiem

# 『The challenge』

We were given `.me` file. Here:

<img width="498" height="415" alt="image" src="https://github.com/user-attachments/assets/fcc3dd48-9624-40b5-9fa3-88f821cf87a6" />

So lets solve!

# 『Solving challenge』
> Solve by: Lylera_

We download this file first. Then, copy to linux file. Then use `strings execute-me`. It is easy. If you don't know what is that command, [click me](https://linux.die.net/man/1/strings)

Here the result:

<img width="890" height="502" alt="image" src="https://github.com/user-attachments/assets/38b3c078-c658-46aa-9e31-c91750632f3d" />

# 『Flag』

We must decode `base64` using [cyberchef](https://gchq.github.io/CyberChef/). Here the result:

<img width="730" height="525" alt="image" src="https://github.com/user-attachments/assets/d808ace6-b032-4209-bede-479f2ba62170" />

```
Flag: compit{execute_on_windows_wsl_linux_based_or_mac???}
```
