import sys, copy
input = sys.stdin.readline

a,b,c = map(int,input().split())

ans = 1

def find(a,b,c):
    global ans

    ans*=a
    ans%=c

    if b == 1:
        return
    elif b%2 == 0:
        find(ans,b//2,c)
    elif b%2 != 0:
        k = ans
        find(ans,b//2,c)
        ans*=k
        ans%=c
    return

find(a,b,c)
print(ans)