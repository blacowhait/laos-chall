from pwn import *
import base64

def enc(plain, key):
	flag = base64.b64encode(plain.encode())
	flag = xor(flag, key)
	return flag

f = open("flag.txt", 'r').read()
res = open("enc.txt", "wb")
res.write(enc(f,"LINZ_IS_HERE"))
res.close()