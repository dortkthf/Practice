from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int,input().split())
tomato = list(list(map(int,input().split())) for i in range(n))
zero = 0
res = 0
queue = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            zero+=1
        elif tomato[i][j] == 1:
            queue.append((i,j,0))
if zero == 0:
    print(0)
    exit(0)

d = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    y,x,day = queue.popleft()
    for i in d:
        ny = y+i[0]
        nx = x+i[1]
        if 0 <= ny < n and 0 <= nx < m and tomato[ny][nx] == 0:
            queue.append((ny,nx,day+1))
            tomato[ny][nx] = 1
            res = day+1
            
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
print(res)