import sys
input = sys.stdin.readline

a,b = map(int,input().split())
c,d = map(int,input().split())
new_a = a*d+c*b
new_b = b*d

if new_a == new_b:
    print(1,1)
    exit(0)
elif new_a > new_b:
    big = new_a
    small = new_b
else:
    big = new_b
    small = new_a

while True:
    temp = big%small
    if temp == 0:
        print(new_a//small,new_b//small)
        break
    big = small
    small = temp