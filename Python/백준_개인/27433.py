import sys
input = sys.stdin.readline

n = int(input())

ans = 1
def fac(n):
    global ans
    if n == 1:
        return
    ans*=n
    return fac(n-1)

if n == 0:
    print(1)
    exit(0)
else:
    fac(n)
    print(ans)