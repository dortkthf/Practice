import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = list(i for i in range(1,n+1))

for k in range(m):
    i,j = map(int,input().split())
    if i == j:
        continue
    elif i == 1:
        if j != n:
            ans = list(reversed(ans[:j])) + ans[j:]
            continue
        ans.reverse()
        continue
    ans = ans[:i-1] + list(reversed(ans[i-1:j])) + ans[j:]

print(*ans)