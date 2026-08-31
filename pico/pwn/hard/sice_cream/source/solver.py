from pwn import *

elf = context.binary = ELF('./sice_cream_patched')
p = process()
libc = ELF('./libc.so.6')

def add(size, data):
    p.sendlineafter('> ', '1')
    p.sendlinafter('How much sice cream do you want?\n> ', str(size))
    p.sendlineafter('What flavor?\n> ', data)
def free(idx):
    p.sendlineafter('> ', '2')
    p.sendlineafter('Which sice cream do you want to eat?\n> ', idx)