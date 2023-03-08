import sys
input = sys.stdin.readline

w = int(input())
w_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

dp = [list(0 for i in range((j*500)+1)) for j in range(w+1)]
r = []

def find(n,weight):
    if n > w:
        return
    if dp[n][weight]:
        return
    dp[n][weight] = 1
    
    find(n+1,weight)
    find(n+1, weight+w_list[n-1])
    find(n+1, abs(weight-w_list[n-1]))
    return

find(0,0)
res = []
for r in m_list:
    if r > 500*w+1:
        res.append('N')
    elif dp[w][r]:
        res.append('Y')
    else:
        res.append('N')
print(*res)