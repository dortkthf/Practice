n,k = map(int,input().split())

def fac(a):
    res = 1
    for i in range(2,a+1):
        res*=i
    return res

ans = fac(n)//fac(k)//fac(n-k)

print(ans%10007)
