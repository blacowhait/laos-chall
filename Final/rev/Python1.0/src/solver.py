from pwn import *
import base64

f = open("enc.txt", 'rb').read()
flag = xor(f, "LINZ_IS_HERE")
print(base64.b64decode(flag))