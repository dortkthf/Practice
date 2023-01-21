a = input()
b = input()

dp = [list(0 for i in range(len(a)+1)) for i in range(len(b)+1)]

for i in range(len(b)):
    for j in range(len(a)):
        if b[i] == a[j]:
            dp[i+1][j+1] = dp[i][j] +1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])

print(dp[len(b)][len(a)])