n = int(input())
nums = list(map(int,input().split()))
nums.sort()
dp = []
for i in range(n):
    if i == 0:
        dp.append(nums[0])
        continue
    dp.append(dp[i-1]+nums[i])
print(sum(dp))