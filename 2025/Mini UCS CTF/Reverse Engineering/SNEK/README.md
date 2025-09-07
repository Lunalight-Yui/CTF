# snek
> Python is an easy language

Author: (unknown)

Solve:

Here's the code:
```
import hashlib

IiIiiI = 63
IiIiii = 63+25

def iIiIiiIiiI(i):
	return i + 2

flag = []
# range is from 63 to 88
for i in range(IiIiiI, IiIiiI):
	flag.append(iIiIiiIiiI(i))
flag = "UCS{" + ''.join(chr(i) for i in flag) + "}"

hashed = hashlib.sha256(flag.encode())
assert hashed.hexdigest() == "54f9d6ef7facbeafe1cc9142955a2f09d9e099df4bce897866e9abd8976fee2f"
print("Flag:", flag)
```

So here's the code to decode:
```
import hashlib

target = "54f9d6ef7facbeafe1cc9142955a2f09d9e099df4bce897866e9abd8976fee2f"

def sha256hex(s):
    return hashlib.sha256(s.encode()).hexdigest()

def try_bruteforce(target_hash):
    # Kita coba parameter yang masuk akal berdasarkan kode yang kamu kasih:
    # - start: 50..70 (ASCII area dekat 63)
    # - length: 1..30
    # - shift (fungsi i+shift): 0..5  (kode pakai +2)
    for start in range(50, 71):
        for length in range(1, 31):
            for shift in range(0, 6):
                chars = [chr(i + shift) for i in range(start, start + length)]
                candidate = "UCS{" + "".join(chars) + "}"
                if sha256hex(candidate) == target_hash:
                    return candidate, (start, length, shift)
    return None, None

if __name__ == "__main__":
    flag, params = try_bruteforce(target)
    if flag:
        print("FOUND FLAG:", flag)
        s, l, sh = params
        print("Parameters found -> start:", s, "length:", l, "shift:", sh)
        print("Verification hash:", sha256hex(flag))
    else:
        print("No match found in the tried parameter ranges.")
```
This is sha-256. Bruteforce to make decoder (sha-256 can't be decode to strings. but they can encode strings to sha-256. So giving bruteforce make sure to check what is the real things of the flag before encode to sha-256):

```
Flags: UCS{ABCDEFGHIJKLMNOPQRSTUVWXY}
```
