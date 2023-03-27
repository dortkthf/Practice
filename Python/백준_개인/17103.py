import sys
input = sys.stdin.readline

t = int(input())
a = 1000001
find = [1]*a
find[0] = 0
find[1] = 0

res = []

for i in range(2,a):
    if find[i] == 1:
        res.append(i)
        for j in range(i+i,a,i):
            find[j] = 0

for _ in range(t):
    n = int(input())
    cnt = 0
    for i in res:
        if i >= n:
            break
        if i <= n-i and find[n-i] == 1:
            cnt+=1
    print(cnt)