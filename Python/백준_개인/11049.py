import sys
input = sys.stdin.readline

n = int(input())
mtx = [[0,0]] + [list(map(int,input().split())) for i in range(n)]
dp = [list(0 for i in range(n+1)) for i in range(n+1)]
maxs = sys.maxsize

for i in range(1,n):
    dp[i][i+1] = mtx[i][0]*mtx[i][1]*mtx[i+1][1]

for i in range(n-1,0,-1):
    for j in range(i,n+1):
        if j>i and dp[i][j] == 0:
            dp[i][j] = maxs
            for k in range(i,j):
                dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]+mtx[i][0]*mtx[k][1]*mtx[j][1])

print(dp[1][n])