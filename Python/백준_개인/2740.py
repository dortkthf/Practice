import sys
input = sys.stdin.readline

n,m = map(int,input().split())
mat1 = [list(map(int,input().split())) for i in range(n)]
m,k = map(int,input().split())
mat2 = [list(map(int,input().split())) for i in range(m)]

rmat2 = [[0 for i in range(m)] for i in range(k)]

for i in range(m):
    for j in range(k):
        rmat2[j][i] = mat2[i][j]

ans = [[] for i in range(n)]

def matrix(q):
    global ans
    for i in range(k):
        res = 0
        for j in range(m):
            res+=mat1[q][j]*rmat2[i][j]
        ans[q].append(res)
    return

for q in range(n):
    matrix(q)

for i in ans:
    print(*i,sep=' ')