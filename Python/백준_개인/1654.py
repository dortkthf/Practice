import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

k,n = map(int,input().split())
kls = []
res = 0
tmp = 0
for i in range(k):
    a = int(input())
    kls.append(a)
    res+=a//n
    tmp+=a%n
    res+=tmp//n
    tmp%=n

kls.sort()

def func(a,b):
    for i in kls:
        a+=i//b
    return a
    
def find(start, end):
    ans = 0
    f1 = 0
    f2 = 0
    f3 = 0
    mid = (start+end)//2
    if mid != 0:
        ans = func(ans,mid)
    if end-start == 1:
        if start != 0:
            f1 = func(f1,start)
        f2 = func(f2,end)
        f3 = func(f3,end+1)
        if f1 >= n and f2 < n:
            print(start)
            exit(0)
        elif f2 >= n and f3 < n:
            print(end)
            exit(0)
    elif ans < n:
        find(start,mid)
        return
    elif ans >= n:
        find(mid,end)
        return

find(0,res)