# xoxo
> They tried to keep a secret in the relationship, but their habits gave everything away.

Author: Vaa

Solve:

We're given a python script, here the script:
```
import os
from Crypto.Util.number import long_to_bytes
from Crypto.Util.strxor import strxor

FLAG = "HCS{placeholder}"

key = os.urandom(4) * 9

flag_bytes = FLAG.encode()

c = strxor(flag_bytes, key[:len(flag_bytes)])
print(c.hex())
# d61a7019ec6a5351aa2d120cf9065b52ec061211c12d1352c12e1056f5065b0de6365e
```

So i ask ai to decode this and this is a python script:

```
# Recover repeating-4-byte XOR key using known plaintext "HCS{" and decrypt the flag.
from Crypto.Util.number import long_to_bytes
from binascii import unhexlify

ct_hex = "d61a7019ec6a5351aa2d120cf9065b52ec061211c12d1352c12e1056f5065b0de6365e"
ct = unhexlify(ct_hex)

# known prefix
known = b"HCS{"
# key repeats every 4 bytes, so key_bytes = ct[:4] XOR known
key4 = bytes([ct[i] ^ known[i] for i in range(4)])
print("Recovered 4-byte key (hex):", key4.hex())

# build full key repeating
full_key = key4 * ( (len(ct) + 3) // 4 )
full_key = full_key[:len(ct)]

# decrypt
pt = bytes([ct[i] ^ full_key[i] for i in range(len(ct))])
print("Decrypted bytes:", pt)
try:
    print("Plaintext:", pt.decode())
except Exception:
    print("Plaintext (repr):", repr(pt))
```

And got a flag

<img width="720" height="102" alt="image" src="https://github.com/user-attachments/assets/2587781f-6896-484f-85cf-9babb45c4ff1" />

```
Flag: HCS{r3p34t1ng_x0r_1s_t00_w34k_xoxo}
```
