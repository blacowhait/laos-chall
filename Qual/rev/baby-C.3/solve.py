arr = [238, 202, 216, 198, 222, 218, 202, 190, 232, 222, 190, 228, 202, 236, 202, 228, 230, 210, 220, 206, 190, 152, 146, 156, 180, 190, 146, 166, 190, 144, 138, 164, 138]
flag = ''

for i in arr:
    flag += chr(i / 2)

print(flag)
