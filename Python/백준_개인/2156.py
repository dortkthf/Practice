# 안마실때, 한잔마실때, 두잔마실때
import sys
input = sys.stdin.readline

n = int(input())
podo = [int(input()) for i in range(n)]
res = [[0,podo[0],0]] + [[0,0,0] for i in range(n-1)]

for i in range(1,n):
    res[i][0] = max(res[i-1])
    res[i][1] = res[i-1][0] + podo[i]
    res[i][2] = res[i-1][1] + podo[i]

print(max(res[n-1]))
