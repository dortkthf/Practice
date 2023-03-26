import sys
input = sys.stdin.readline

res = list(map(int,input().split()))
res.sort()

if (res[0] == res[1] and res[1] == res[2]) or res[0]+res[1] > res[2]:
    print(sum(res))
elif res[0] + res[1] <= res[2]:
    a = res[2] - res[0] - res[1]
    res[2] -= (a+1)
    print(sum(res))