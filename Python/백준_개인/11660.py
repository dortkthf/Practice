n,m = map(int,input().split())
table = []
dp = []
dp_col = [[] for i in range(n)]
for i in range(n):
    nums = list(map(int,input().split()))
    table.append(nums)
    tmp = []
    for j in range(n):
        if i == 0:
            dp_col[j].append(nums[j])
        else:
            dp_col[j].append(nums[j]+dp_col[j][i-1])
        if i == 0 and j == 0:
            tmp.append(nums[j])
        elif i == 0 and j>0:
            tmp.append(nums[j]+tmp[j-1])
        elif i>0 and j == 0:
            tmp.append(dp[i-1][-1]+nums[j])
        elif i >0 and j>0:
            tmp.append(nums[j]+tmp[j-1])
    dp.append(tmp)

for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    if x1 == 1 and y1 == 1:
        print(dp[x2-1][y2-1])
    elif x1 == 1 and y1>1:
        print(dp[x2-1][y2-1]-)