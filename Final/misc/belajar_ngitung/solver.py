from pwn import *
from sys import *


#HOST = "chall.agrihack-csi.com"
#PORT = 19000
#p = remote(HOST,PORT)
p = process("./ngitung")

i = 2
while(1):
	p.sendline(str(i))
	print(p.recv())
	i += 1

p.interactive()