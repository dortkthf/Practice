import sys
input = sys.stdin.readline

m,n = map(int,input().split())
maps = [list(map(int,input().split())) for i in range(m)]
dp = [list(0 for i in range(n)) for i in range(m)]

d = [[-1,0],[0,1],[1,0],[0,-1]]
def find(a,b):
    for k in d:
        if k[0]+a >= 0 and k[0]+a < m and k[1]+b >=0 and k[1]+b < n and maps[a][b] > maps[k[0]+a][k[1]+b] and dp[k[0]+a][k[1]+b] != -1:
            if dp[k[0]+a][k[1]+b] != -1 and dp[k[0]+a][k[1]+b] >0:
                dp[a][b] += dp[k[0]+a][k[1]+b]
                continue
            elif k[0]+a == m-1 and k[1]+b == n-1:
                dp[a][b] += 1
                return
            find(k[0]+a,k[1]+b)
            if dp[k[0]+a][k[1]+b] != -1:
                dp[a][b] += dp[k[0]+a][k[1]+b]
    else:
        if dp[a][b] == 0:
            dp[a][b] = -1
find(0,0)
if dp[0][0] == -1:
    if m == 1 and n == 1:
        print(1)
    else:
        print(0)
else:
    print(dp[0][0])
