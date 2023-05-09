import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = [0] + list(map(int,input().split()))
c = [0] + list(map(int,input().split()))
dp = [list(0 for i in range(sum(c)+1)) for i in range(n+1)]
result = sum(c)

for i in range(1,n+1):
    byte = a[i]
    cancel = c[i]

    for j in range(1,sum(c)+1):
        if j < cancel:
            dp[i][j] = dp[i-1][j]
        else:`
            dp[i][j] = max(byte+dp[i-1][j-cancel],dp[i-1][j])
        `
        if dp[i][j] >= m:
            result = min(j,result)

print(result)