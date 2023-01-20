n = int(input())

ls = [list(map(int,input().split())) for i in range(n)]
ls.sort()
right = []

for i in ls:
    right.append(i[1])

dp = [1 for i in range(n)]
for i in range(1,n):
    for j in range(i):
        if right[i]>right[j]:
            dp[i] = max(dp[j]+1,dp[i])

print(n-max(dp))