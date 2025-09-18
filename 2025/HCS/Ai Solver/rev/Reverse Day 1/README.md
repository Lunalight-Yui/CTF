# Reverse Day 1
> Ketika pertama kali belajar reverse engineering, biasanya challenge bisa di-solved cukup dengan strings. Sayangnya, kali ini strings saja belum bisa untuk mendapatkan flag.

Author: erzyyyy

Solve:

We're given chall file. if we use `strings`, here the result

<img width="683" height="880" alt="image" src="https://github.com/user-attachments/assets/84a2ee20-b066-4f41-8a0c-48523a1df050" />

i ask Ai to solve this and they use python script. Here the result:
```
# Reconstruct the 23-byte expected flag by using the immediates found in the disassembly.
# We observed these immediates in little-endian placement:
# movabs rax,0x3b283b2c250d1d16  -> bytes little-endian of that 8-byte value
# movabs rdx,0x3b012d37013b2d2c  -> bytes little-endian
# mov dword [rbp-0x40],0x2727243f -> 4 bytes little-endian
# mov word  [rbp-0x3c],0x2727       -> 2 bytes little-endian
# mov byte  [rbp-0x3a],0x23         -> 1 byte
# XOR key at rbp-0x69 is 0x5e
vals = {
    'v1': 0x3b283b2c250d1d16,
    'v2': 0x3b012d37013b2d2c,
    'd1': 0x2727243f,
    'w1': 0x2727,
    'b1': 0x23,
    'key': 0x5e
}
import struct
b = bytearray()
# little endian packing
b += struct.pack('<Q', vals['v1'])
b += struct.pack('<Q', vals['v2'])
b += struct.pack('<I', vals['d1'])
b += struct.pack('<H', vals['w1'])
b += struct.pack('<B', vals['b1'])
len_b = len(b)
print("Constructed bytes length:", len_b)
print("Hex:", b.hex())
# apply XOR key to each byte and produce string
flag_bytes = bytes([x ^ vals['key'] for x in b])
try:
    flag = flag_bytes.decode('utf-8')
except:
    # show repr if non-utf8
    flag = ''.join(chr(x) if 32<=x<=126 else '\\x%02x'%x for x in flag_bytes)
print("Flag bytes after XOR:", flag_bytes)
print("Flag string (decoded or escaped):")
print(flag)
```
```
Flag: HCS{reverse_is_eazyyyy}
```
