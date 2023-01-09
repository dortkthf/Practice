t = int(input())
def fac(a):
    ans = 1
    for i in range(2,a+1):
        ans*=i
    return ans

def cal(a,b):
    return fac(b)//fac(a)//fac(b-a)

for _ in range(t):
    a,b = map(int,input().split())
    print(cal(a,b))