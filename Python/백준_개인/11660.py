import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = [list(map(int,input().split())) for i in range(n)]
dp = [list(0 for i in range(n)) for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            dp[i][j] = nums[i][j]
        elif i == 0 and j > 0:
            dp[i][j] = nums[i][j] + dp[i][j-1]
        elif i > 0 and j == 0:
            dp[i][j] = nums[i][j] + dp[i-1][j]
        elif i > 0 and j > 0:
            dp[i][j] = nums[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    if x1 == x2 and y1 == y2:
        print(nums[x1-1][y1-1])
    elif x1 == 1 and y1 == 1:
        print(dp[x2-1][y2-1])
    elif x1 == 1 and y1 > 1:
        print(dp[x2-1][y2-1] - dp[x2-1][y1-2])
    elif y1 == 1 and x1 > 1:
        print(dp[x2-1][y2-1] - dp[x1-2][y2-1])
    elif x1 > 1 and y1 > 1:
        print(dp[x2-1][y2-1] - dp[x2-1][y1-2] - dp[x1-2][y2-1] + dp[x1-2][y1-2] )