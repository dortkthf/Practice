import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
chess = [input().rstrip() for i in range(n)]
dp_black = [list(0 for i in range(m+1)) for i in range(n+1)]
dp_white = [list(0 for i in range(m+1)) for i in range(n+1)]
res = []
for i in range(1,n+1):
    for j in range(1,m+1):
        if (i+j)%2 == 0:
            if chess[i-1][j-1] == 'B':
                dp_black[i][j] = dp_black[i-1][j] + dp_black[i][j-1] - dp_black[i-1][j-1]
                dp_white[i][j] = dp_white[i-1][j] + dp_white[i][j-1] - dp_white[i-1][j-1] + 1
            else:
                dp_black[i][j] = dp_black[i-1][j] + dp_black[i][j-1] - dp_black[i-1][j-1] + 1
                dp_white[i][j] = dp_white[i-1][j] + dp_white[i][j-1] - dp_white[i-1][j-1]
        elif (i+j)%2 != 0:
            if chess[i-1][j-1] == 'W':
                dp_black[i][j] = dp_black[i-1][j] + dp_black[i][j-1] - dp_black[i-1][j-1]
                dp_white[i][j] = dp_white[i-1][j] + dp_white[i][j-1] - dp_white[i-1][j-1] + 1
            else:
                dp_black[i][j] = dp_black[i-1][j] + dp_black[i][j-1] - dp_black[i-1][j-1] + 1
                dp_white[i][j] = dp_white[i-1][j] + dp_white[i][j-1] - dp_white[i-1][j-1]

for i in range(k,n+1):
    for j in range(k,m+1):
        res.append(dp_black[i][j]-dp_black[i-k][j]-dp_black[i][j-k]+dp_black[i-k][j-k])
        res.append(dp_white[i][j]-dp_white[i-k][j]-dp_white[i][j-k]+dp_white[i-k][j-k])

print(min(res))