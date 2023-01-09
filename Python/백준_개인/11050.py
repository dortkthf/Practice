n,k = map(int,input().split())

def fac(a):
    ans = 1
    for i in range(2,a+1):
        ans*=i
    return ans

def cal(a,b):
    return fac(a)//fac(b)//fac(a-b)

print(cal(n,k))

