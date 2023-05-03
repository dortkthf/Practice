from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
maps = list(list(input()) for i in range(n))
for i in range(n):
    for j in range(m):
        maps[i][j] = int(maps[i][j])

queue = deque()
queue.append((0,0,1,0))

d = [(1,0),(-1,0),(0,1),(0,-1)]

bcheck = list(list(0 for i in range(m)) for i in range(n))
check = list(list(0 for i in range(m)) for i in range(n))
bcheck[0][0] = 1
check[0][0] = 1
n,m = n-1, m-1

while queue:
    y,x,num,bk = queue.popleft()
    if y == n and x == m:
        print(num)
        exit(0)
    for i in d:
        ny,nx = y+i[0],x+i[1]
        if 0<=ny<=n and 0<=nx<=m:
            if bk == 0 and check[ny][nx] == 0:
                if maps[ny][nx] == 0:
                    check[ny][nx] = 1
                    queue.append((ny,nx,num+1,bk))
                elif maps[ny][nx] == 1:
                    bcheck[ny][nx] = 1
                    queue.append((ny,nx,num+1,bk+1))
            elif bk == 1 and bcheck[ny][nx] == 0:
                if maps[ny][nx] == 0:
                    bcheck[ny][nx] = 1
                    queue.append((ny,nx,num+1,bk))
                
print(-1)