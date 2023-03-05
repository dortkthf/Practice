import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = list(0 for i in range(n))

for i in range(m):
    i,j,k = map(int,input().split())
    if i == j:
        ans[i-1] = k
        continue
    for a in range(i-1,j):
        ans[a] = k

print(*ans,sep=' ')