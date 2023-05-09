from collections import deque
import sys
input = sys.stdin.readline

m,n,h = map(int,input().split())
tomato = []
for _ in range(h):
    tmp = []
    for i in range(n):
        tmp.append(list(map(int,input().split())))
    tomato.append(tmp)

zero = 0
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                zero+=1
            elif tomato[i][j][k] == 1:
                queue.append((i,j,k,0))

if zero == 0:
    print(0)
    exit(0)

d = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

while queue:
    h0,n0,m0,day = queue.popleft()
    for i in d:
        nh,nn,nm = h0+i[0],n0+i[1],m0+i[2]
        if 0 <= nh < h and 0 <= nn < n and 0 <= nm < m and tomato[nh][nn][nm] == 0:
            queue.append((nh,nn,nm,day+1))
            tomato[nh][nn][nm] = 1
            
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
print(day)