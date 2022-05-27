import zlib
import random

enc = open('py.rus').read()
random.seed(0xcafebabe)
print zlib.decompress("".join([chr(ord(i)^random.randint(0,0xff)) for i in enc]))