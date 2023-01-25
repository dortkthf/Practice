import sys
input = sys.stdin.readline

n,k = map(int,input().split())
dp = [0 for i in range(k+1)]

# 1 번째 방법
# ws = [0]
# vs = [0]

# for i in range(n):
#     w,v = map(int,input().split())
#     ws.append(w)
#     vs.append(v)

# for i in range(1,n+1):
#     for j in range(1,k+1):
#         if ws[i] <= j:
#             dp[j] = max(dp[j], dp[j-ws[i]]+vs[i])
#         continue

# print(dp[-1])

# 2 번째 방법 K값이 뒤에서부터 진행되어야함
# for i in range(n): 
#     w,v = map(int,input().split())
#     for j in range(k,0,-1):
#         if w<=j:
#             dp[j] = max(dp[j], dp[j-w]+v)

# print(dp[-1])

