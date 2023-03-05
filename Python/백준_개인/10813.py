import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = [i for i in range(1,n+1)]

for a in range(m):
    i,j = map(int,input().split())
    if i == j:
        continue
    tmp = ans[i-1]
    ans[i-1] = ans[j-1]
    ans[j-1] = tmp

print(*ans)