import sys
input = sys.stdin.readline
t = int(input())

def sosu(a):
    for i in range(2,int(a**(1/2))+1):
        if a%i == 0:
            return False
    return True

for _ in range(t):
    n = int(input())

    if n == 1 or n == 0:
        print(2)
    elif n == 2:
        print(2)
    else:
        for i in range(n,n+1000):
            if sosu(i):
                print(i)
                break