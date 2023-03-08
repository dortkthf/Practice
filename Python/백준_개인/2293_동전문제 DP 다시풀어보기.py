import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = []
for i in range(n):
    c = int(input())
    if c <= k:
        coins.append(c)

d = [0 for i in range(k+1)]
d[0] = 1

for c in coins:
    for j in range(c,k+1):
        d[j] += d[j-c]

print(d[-1])