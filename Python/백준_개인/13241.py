import sys
input = sys.stdin.readline

a,b = map(int,input().split())
if a == b:
    print(a)
    exit(0)
elif a > b:
    big = a
    small = b

else:
    big = b
    small = a

while True:
    temp = big%small
    if temp == 0:
        print(small*a//small*b//small)
        break
    big = small
    small = temp