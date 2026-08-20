# 『write-me』
> just write the key on it bro ps. key is rizztech

Author: requiiem

# 『The challenge』

We were given `.py` files. Here the screenshot:

<img width="497" height="414" alt="image" src="https://github.com/user-attachments/assets/783410c1-83cb-43e8-890f-d33fe46f3338" />

# 『Solving challenge』
> Solve by: Lylera_

To solve this, open the `.py` files. Here the code:

```
# encrypted = "compit{REDACTED}"
data = "1106170a1d11180c1b19251e1d153c0c1b19251e1d153c0c1b1907"
key = "" # write the key here # rizztech

encrypted = bytes.fromhex(data)

flag = []
for i in range(len(encrypted)):
  flag.append(chr(encrypted[i] ^ ord(key[i % len(key)])))
  # flag.append(chr(ord(encrypted[i]) ^ ord(key[i % len(key)])))
# final = ''.join(flag).encode().hex()
final = ''.join(flag)

print(final)

# commented code is the generator
```

# 『Flag』

To solve this, write the key were given on description. Here the result:

<img width="687" height="395" alt="image" src="https://github.com/user-attachments/assets/dd3c8ee5-1365-4de9-9727-4b598e4e1055" />

i used [gdb online](https://www.onlinegdb.com/) to solve this one. Easy right?

```
Flag: compit{dip_dip_dip_dip_dip}
```
