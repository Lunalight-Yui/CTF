# Password
> Did you know the password? Resources:
> https://dogbolt.org/
> https://hex-rays.com/ida-pro
> https://binary.ninja/
> https://www.nsa.gov/ghidra
> https://en.wikipedia.org/wiki/Ptrace
> https://www.man7.org/linux/man-pages/man1/strings.1.html 

Author: Hanz

Solve:

Before we solve it, you can get the file by using:

```
wget https://minictf.ucs.or.id/files/6e49b6788965fe8c9e982cf964a0cef4/chal?token=eyJ1c2VyX2lkIjoyNywidGVhbV9pZCI6bnVsbCwiZmlsZV9pZCI6MTN9.aLz9Kw.IRuzLUF5L2kGghSNbOV9fDVkNBw
```

After done, you can see the file that can't not access, right? welp no, you can. But the file might be different character. On linux, you can use this command

```
chmod +x <file>
```
for example, i use this: `chmod +x chal`. After that, i can open (before you open, make sure directory on terminal and directory file's downloaded has same. If you place on downloads, you must `cd downloads`. if it is done, you can 
go to next step. if it is undone, try `ls` first. then `cd <file/category you placed>`. If the file still on zip file, you can use `unzip <file>.zip`. That's it) this file using command `./chal`. the result like this:

<img width="349" height="70" alt="image" src="https://github.com/user-attachments/assets/a034609b-cd46-4b42-b040-d1ea86c61ecf" />

If you input (let say) `a`, the result will be like this: 

<img width="99" height="43" alt="image" src="https://github.com/user-attachments/assets/6b403a2a-1efc-49d4-bc22-5a01e2c5e960" />

Then how we bypass this one and searching flags inside of this file? Well, simple. Remember, you can use description to see hint that given to you. If you want simple, follow me.

Lets go learn about strings. What's that? strings a utility used to extract printable character sequences (strings) from files. You might familiar in the coding about `Hello world!`, right?

That's call strings in coding. It should like this in coding `print("Hello world!")`. But in linux, this command can print the file that hidden containing about characters. If you want to learn about strings,
this one:
> https://linux.die.net/man/1/strings
> https://www.man7.org/linux/man-pages/man1/strings.1.html

Alright, lets go use `strings`. How we use it? simple
```
strings <file>
```
Example: `strings chal` and the result:

<img width="236" height="838" alt="Screenshot 2025-09-06 104223" src="https://github.com/user-attachments/assets/d14c0401-3379-49e9-93aa-d73fb599defa" />

And here you go. 
```
Flag: UCS{certified_reverse_engineering_beginner}
```
