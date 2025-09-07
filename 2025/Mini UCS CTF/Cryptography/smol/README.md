# Smol
> the params seems to be a bit weird... as long as it works i guess :shrug:

Author: etern1ty

Solve:

```
So heres the code:

from Cryptodome.Util.number import *

import random

with open('flag.txt','rb') as f:
    m = bytes_to_long(f.read().strip())

def blum_prime(bits=512):
    while True:
        p = getPrime(bits)
        if p % 4 == 3:
            return p

p = blum_prime(512)
q = blum_prime(512)
n = p * q

phi = (p - 1) * (q - 1)

bound = max(3, int(n**0.25) // 8) 
while True:
    d = random.randint(2, bound)
    if GCD(d, phi) == 1:
        break

e = inverse(d, phi)
c = pow(m, e, n)

with open('output.txt','w') as f:
    f.write(f"{n}\n{e}\n{c}\n")
```

So here's the output.txt:
```
125606426618683744569134709537229409847421464585289553423863427771172910844703678731033426331462375424565248241588429702292145832115917467941828538845582804612420829599669844298961278630582192829448264450753014845404825560635149868035660736393523243109244896401814742188807642775968535926280138060939861300053
9666179459703310192454478330648342818473333568018369928510746806341173740146160233605591978324585983718596879674618578754977241519535236740915717246308430624375962494798014507164775160066551160597181901895180506378581598653797298034637136494875017451977355815136399782428761557604010182808455572083614504217
124045709172602859974825506757868289698407617368632021329766203716320682339272589456269815078366199000220066385164852368854230554411375867857159899501209562482703211032858112555616553894272985581207080354617735890010955081724521533973397203370681556701583664727047736082782678231976706744897069101960518231354
```

This is RSA. We can use wiener's attack. What's that? Wiener's attack is cryptography attacking RSA. The attack uses continued fraction representation to expose the private key d when d is small.
Hope you understand, but if i know more later, i will update this one or making some new file to explain on cryptography folder. Just wait!

Here are the code i ask on gpt to find it:
```
from Cryptodome.Util.number import *
from math import isqrt

# Data dari output.txt
n = 125606426618683744569134709537229409847421464585289553423863427771172910844703678731033426331462375424565248241588429702292145832115917467941828538845582804612420829599669844298961278630582192829448264450753014845404825560635149868035660736393523243109244896401814742188807642775968535926280138060939861300053
e = 9666179459703310192454478330648342818473333568018369928510746806341173740146160233605591978324585983718596879674618578754977241519535236740915717246308430624375962494798014507164775160066551160597181901895180506378581598653797298034637136494875017451977355815136399782428761557604010182808455572083614504217
c = 124045709172602859974825506757868289698407617368632021329766203716320682339272589456269815078366199000220066385164852368854230554411375867857159899501209562482703211032858112555616553894272985581207080354617735890010955081724521533973397203370681556701583664727047736082782678231976706744897069101960518231354

# --- Helper functions ---
def continued_fraction(numerator, denominator):
    """Compute continued fraction expansion of numerator/denominator"""
    cf = []
    while denominator:
        a = numerator // denominator
        cf.append(a)
        numerator, denominator = denominator, numerator - a * denominator
    return cf

def convergents(cf):
    """Compute convergents from a continued fraction expansion"""
    convs = []
    for i in range(len(cf)):
        num, den = 1, 0
        for j in reversed(cf[:i+1]):
            num, den = den + num * j, num
        convs.append((num, den))
    return convs

def wiener_attack(e, n):
    cf = continued_fraction(e, n)
    for k, d in convergents(cf):
        if k == 0: 
            continue
        if (e*d - 1) % k != 0:
            continue
        phi = (e*d - 1) // k
        s = n - phi + 1
        disc = s*s - 4*n
        if disc >= 0:
            t = isqrt(disc)
            if t*t == disc and (s+t) % 2 == 0:
                return d
    return None

# --- Run attack ---
d = wiener_attack(e, n)
print("[+] Recovered d:", d)

m = pow(c, d, n)
flag = long_to_bytes(m)
print("Flag:", flag.decode(errors="ignore"))
```

And the result:
<img width="951" height="69" alt="image" src="https://github.com/user-attachments/assets/37fa1c43-f1ec-4193-b5dd-c45f48d19967" />

```
flag: UCS{sdskdjsjdaopjdpdeawpodaopdaksd_congrats_you_now_know_an_attack_for_rsa_6574657277617368657265}
```
