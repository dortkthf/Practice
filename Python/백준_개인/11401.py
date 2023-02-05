import sys
input = sys.stdin.readline

n,k = map(int,input().split())

p = 1000000007

def fac(a):
    res = 1
    for i in range(1,a+1):
        res*=i
        res%=p
    return res

n2 = fac(n)
p2 = fac(n-k)*fac(k)%p

ans = 1
def find(a,b,c):
    global ans
    
    ans*=a
    ans%=c

    if b==1:
        return
    elif b%2 == 0:
        find(ans,b//2,c)
        return
    elif b%2 != 0:
        k = ans
        find(ans,b//2,c)
        ans*=k
        ans%=c
        return

find(p2,p-2,p)

print(n2*ans%p)