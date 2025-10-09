# 『repo』
> mana ....

Author: hyall

# 『The challenge』

We were give zip file name `repo`. If we unzip, here the inside folder:

<img width="1242" height="165" alt="image" src="https://github.com/user-attachments/assets/5823f260-40e8-44fb-a385-860b0305a6ae" />

So lets solve!

# 『Solving challenge』
> solve by: pemula

Open linux

<img width="940" height="111" alt="image" src="https://github.com/user-attachments/assets/589ddc51-3b82-4769-90d3-b88645eeb1f9" />

After that unzip `repo.zip`

<img width="689" height="73" alt="image" src="https://github.com/user-attachments/assets/bf88a136-77f4-42de-9f60-4f05f3acfbe5" />

go to `repo` using `cd` then use `ls -all` to see all file. here the result:

<img width="756" height="185" alt="image" src="https://github.com/user-attachments/assets/ff00db9b-b7da-4b4d-b5ba-6d2a5bb96e1f" />

go to `.git`

<img width="801" height="30" alt="image" src="https://github.com/user-attachments/assets/7e4723bb-82e4-48ff-885e-68769020e548" />

# 『Flag』

Use `cat` to see `COMMIT_EDITMSG` file. Here the result:

<img width="813" height="49" alt="image" src="https://github.com/user-attachments/assets/f030c1fb-24e5-4191-851e-445acec74359" />

```
Flag: compit{git_history_never_lies}
```
