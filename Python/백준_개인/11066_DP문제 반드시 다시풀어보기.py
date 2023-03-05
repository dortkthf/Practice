import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    dp = [list(0 for i in range(n+1)) for i in range(n+1)]
    slst = [0 for i in range(n+1)]
    for i in range(1,n+1):
        slst[i] = slst[i-1]+lst[i-1]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i+1 == j:
                dp[i][j] = lst[i-1]+lst[j-1]
                continue
    for a in range(n,0,-1):
        for b in range(1,n+1):
            if a<b and dp[a][b] == 0:
                dp[a][b] = min(list(dp[a][k]+dp[k+1][b] for k in range(a,b))) + slst[b]-slst[a-1]
    print(dp[a][b])