import sys
input = sys.stdin.readline

n = int(input())
house = [list(map(int,input().split())) for i in range(n)]
res = [[] for i in range(n)]

for i in range(n):
    for j in range(3):
        nr = [0,1,2]
        if i == 0:
            res[i].append(house[i][j])
        else:
            nr.remove(j)
            res[i].append(house[i][j]+min(res[i-1][nr[0]],res[i-1][nr[1]]))
print(min(res[n-1]))