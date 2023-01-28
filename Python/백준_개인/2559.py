import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(map(int,input().split()))

dp = [0 for i in range(n)]
dp[0] = nums[0]
res = []

for i in range(1,n):
    dp[i] = nums[i] + dp[i-1]

for i in range(k-1,n):
    if i == k-1:
        res.append(dp[i])
        continue
    elif n == k:
        print(dp[k-1])
        break
    res.append(dp[i]-dp[i-k])
else:
    print(max(res))