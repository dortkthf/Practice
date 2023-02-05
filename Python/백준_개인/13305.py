import sys
input = sys.stdin.readline

n = int(input())
way = list(map(int,input().split()))
oil = list(map(int,input().split()))

ans = 0
for i in range(n-1):
    if i == 0:
        s = oil[i]
        ans+=way[i]*s
    elif s > oil[i]:
        s = oil[i]
        ans+=way[i]*s
    else:
        ans+=way[i]*s
print(ans)