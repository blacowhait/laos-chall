from Crypto.PublicKey import RSA

key = RSA.generate(4096, e=5)
msg = open("flag.txt","rb").read().strip()
m = int(msg.encode("hex"), 16)
c = pow(m, key.e, key.n)

print 'n = {}'.format(key.n)
print 'e = {}'.format(key.e)
print 'c = {}'.format(c)
# printed on output.txt
