import sys
sys.setrecursionlimit(10**8)

n = int(input())

chess = list(list(0 for i in range(n)) for i in range(n))

d = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def queens(r,c,i):
    chess[r][c] = 1
    if r+d[i][0]>=0 and r+d[i][0]<n and c+d[i][1]>=0 and c+d[i][1]<n:
            r,c = r+d[i][0],c+d[i][1]
            queens(r,c,i)
            return

def dqueens(r,c,i):
    chess[r][c] = 0
    if r+d[i][0]>=0 and r+d[i][0]<n and c+d[i][1]>=0 and c+d[i][1]<n:
            r,c = r+d[i][0],c+d[i][1]
            dqueens(r,c,i)
            return

def queen(r,c):
    chess[r][c] = 1
    br,bc = r,c
    for i in d:
        basei = d.index(i)
        r,c = br,bc
        if r+i[0]>=0 and r+i[0]<n and c+i[1]>=0 and c+i[1]<n:
            r,c = r+i[0],c+i[1]
            queens(r,c,basei)
            continue
    return

def dqueen(r,c):
    chess[r][c] = 0
    br,bc = r,c
    for i in d:
        basei = d.index(i)
        r,c = br,bc
        if r+i[0]>=0 and r+i[0]<n and c+i[1]>=0 and c+i[1]<n:
            r,c = r+i[0],c+i[1]
            dqueens(r,c,basei)
            continue
    return

res = 0
cnt = 0

def sol():
    global cnt
    global res
    for i in range(n):
        for j in range(n):
            if cnt == n:
                res+=1
                cnt-=1
                dqueen(i,j)
                return
            else:
                if chess[i][j] == 0:
                    queen(i,j)
                    cnt+=1
                    sol()
                    cnt-=1
            dqueen(i,j)
            continue
    return

print(sol())