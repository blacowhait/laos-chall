import os
import zlib
import random

def compress_file():
    return zlib.compress("".join([open(i).read() for i in os.listdir('.')]))

def encrypt_file(plaintext, seed=0xcafebabe):
    random.seed(seed)
    return "".join([chr(ord(i)^random.randint(0,0xff)) for i in plaintext])

def main():
    enc = open('py.rus', 'wb')
    enc.write(encrypt_file(compress_file()))
    enc.close()

if __name__ == "__main__":
    main()