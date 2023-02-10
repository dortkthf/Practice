import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m = map(int,input().split())
namu = list(map(int,input().split()))
if n == 1:
    print(namu[0]-m)
    exit(0)
min_namu = min(namu)
max_namu = max(namu)
if min_namu == max_namu:
    a = sum(namu) - m
    print(a//n)
    exit(0)
def func(cut):
    global namu
    ans = 0
    for i in namu:
        if (i-cut)<0:
            continue
        ans+=(i-cut)
    return ans

def namus(min_,max_):
    mid = (min_+max_)//2
    a = func(mid)
    b = 0
    c = 0
    d = 0
    if max_-min_ == 1:
        b = func(max_)
        c = func(min_)
        d = func(max_+1)
        if c >= m and b < m:
            print(min_)
            exit(0)
        elif b >= m and d < m:
            print(max_)
            exit(0)
    elif a >= m:
        namus(mid,max_)
        return
    elif a < m:
        namus(min_,mid)
        return

namus(0,max_namu)