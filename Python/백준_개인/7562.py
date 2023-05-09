from collections import deque
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l = int(input())
    chess = list(list(0 for i in range(l)) for i in range(l))
    sx,sy = map(int,input().split())
    ex,ey = map(int,input().split())
    
    chess[sx][sy] = 1
    
    queue = deque()
    queue.append((sx,sy,0))
    
    d = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
    
    while queue:
        x,y,time = queue.popleft()
        if x == ex and y == ey:
            print(time)
            break
        for i in d:
            if 0 <= x+i[0] < l and 0 <= y+i[1] < l and chess[x+i[0]][y+i[1]] == 0:
                queue.append((x+i[0],y+i[1],time+1))
                chess[x+i[0]][y+i[1]] = 1