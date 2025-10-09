# 『baby_foren』
> buka bang

Author: hyall

# 『The challenge』

We're given this challenge. Here is the file challenge.png:

<img width="745" height="432" alt="image" src="https://github.com/user-attachments/assets/2a4c22c7-0926-44e4-a905-2f871b2e59ad" />

This is unique, so let solve!
# 『Solving challenge』
> solve by pemula

Open this file using hxd tools, here the result:

<img width="689" height="610" alt="image" src="https://github.com/user-attachments/assets/50e75cdb-048a-42b1-875e-cff85dbae33f" />

As you can see, there are no signature file of png. We must fix the hex decimal by using this `89 50 4E 47 0D 0A 1A 0A`


# 『Flag』
After fix this header signature file, we can open chall.jpg and if we open it: 

<img width="940" height="489" alt="image" src="https://github.com/user-attachments/assets/9cbc3d14-bee9-4cd4-8c25-d518afb996c7" />

```
Flag: compit{y0u_f1x3d_Th3_h3ad3r_C0ngr4t5}
```
