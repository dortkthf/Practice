import sys
input = sys.stdin.readline

n = int(input())
res = [list(map(int,input().split())) for i in range(n)]
if n == 1:
    print(0)
    exit(0)
res.sort()
a = res[-1][0] - res[0][0]

res.sort(key = lambda x:x[1])
b = res[-1][1] - res[0][1]
print(a*b)