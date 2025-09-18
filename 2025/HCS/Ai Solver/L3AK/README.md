# L3AK
> what is what?

Author: etern1ty

Solve:

We're give 2 file, 1 output and 1 python script

Python script:
```
from Crypto.Util.number import *
with open('flag.txt') as f:
    flag = f.read().strip()

p = getPrime(512)
q = getPrime(512)
n = p * q
phi = (p - 1) * (q - 1)

e = 65537
d = inverse(e, phi)
what = d % (p - 1)

ct = pow(bytes_to_long(flag.encode()), e, n)
with open('output.txt', 'w') as f:
    f.write(f'n = {n}\n')
    f.write(f'ct = {ct}\n')
    f.write(f'what = {what}\n')
```

Output.txt:
```
n = 132424945097525850654214822436841749617596013766516589461846053019923921509419349878188173267137393388564369574894943951802964034938666342594121858359017467945336230806773103437033058400722533249173019431218833060574032187854004778243330232248639993250668984287478087484530899867973181768171106834615858816947
ct = 8690256152525015206584791844752543379719744787620368046544606811870676380837374553817755653019413372016870108768104936568432345008226950086769230094097164464486596908050930851678115904352532562944170575365724833300330295692157262447360439786705110831106538310141401194897207768598781335529794463310318530218
what = 4701066001566933468539295457165541117336002410834834617743586840140912396231299819496271034686173752299173098904260222360140687146281504574213995930648721
```

How to solve it. I use ai to make script for decode this RSA:
```
#!/usr/bin/env python3
# one_shot.py — minimal exploit to get the flag from output.txt

import re, math
from pathlib import Path

TXT = Path("output.txt").read_text()
def get_int(k): 
    return int(re.search(rf"{k}\s*=\s*([0-9]+)", TXT).group(1))

n = get_int("n"); ct = get_int("ct"); what = get_int("what")
e = 65537

# coba dengan a = 2 dulu (sering cukup)
a = 2
g = math.gcd(pow(a, e*what - 1, n) - 1, n)
if g == 1 or g == n:
    # kalau gagal, coba beberapa basis cepat
    for a_try in [3,5,7,11,13]:
        g = math.gcd(pow(a_try, e*what - 1, n) - 1, n)
        if 1 < g < n:
            a = a_try
            break

if not (1 < g < n):
    raise SystemExit("Fail: couldn't find factor (try more bases)")

p = g; q = n // p
phi = (p-1)*(q-1)
d = pow(e, -1, phi)        # Python3.8+
m = pow(ct, d, n)
# convert to bytes
flag = m.to_bytes((m.bit_length()+7)//8, "big").decode(errors="ignore")
print(flag)
```

So here the result:

<img width="463" height="90" alt="image" src="https://github.com/user-attachments/assets/cf6cf7d6-7a8c-41b0-89e5-f1813bb342d0" />

```
Flag: HCS{leak_l3ak_l34k_i_hate_leaks_65746572}
```
