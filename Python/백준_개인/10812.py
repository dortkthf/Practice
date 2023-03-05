import sys
input = sys.stdin.readline

n,m = map(int, input().split())
ans = list(i for i in range(1,n+1))
for i in range(m):
    left,right,mid = map(int,input().split())
    if left == right or left == mid:
        continue
    if left == 1:
        ans = ans[mid-1:right] + ans[:mid-1] + ans[right:]
        continue
    ans = ans[:left-1] + ans[mid-1:right] + ans[left-1:mid-1] + ans[right:]

print(*ans)