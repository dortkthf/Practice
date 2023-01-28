import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0 for i in range(n)]
dp[0] = nums[0]

for i in range(1,n):
    dp[i] = nums[i]+dp[i-1]

for _ in range(m):
    i,j = map(int,input().split())
    if i == 1:
        print(dp[j-1])
        continue
    print(dp[j-1]-dp[i-2])
