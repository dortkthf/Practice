import sys
input = sys.stdin.readline

while True:
    a = list(map(int,input().split()))
    if sum(a) == 0:
        break
    a.sort()
    if a[0] == a[1] == a[2]:
        print('Equilateral')
    elif a[0]+a[1] <= a[2]:
        print('Invalid')
    elif a[0] == a[1] or a[1] == a[2]:
        print('Isosceles')
    elif a[0] != a[1] and a[1] != a[2] and a[2] != a[0]:
        print('Scalene')