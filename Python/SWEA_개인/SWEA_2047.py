phrase = input()

for i in phrase :
    if ord(i) >= 97 and ord(i) <=122:
        i = chr(ord(i)-32)
    print(i,end='')