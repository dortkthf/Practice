import sys
input = sys.stdin.readline

n = int(input())
trg = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    if i == 0:
        continue
    for j in range(len(trg[i])):
        if j == 0:
            trg[i][j] += trg[i-1][0]
            continue
        if j == len(trg[i])-1:
            trg[i][j] += trg[i-1][j-1]
            continue
        trg[i][j] += max(trg[i-1][j-1],trg[i-1][j])

print(max(trg[n-1]))
