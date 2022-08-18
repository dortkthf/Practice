t = int(input())
for _ in range(t):
    x,y,k = map(int,input().split())
    land = [list(0 for i in range(x)) for i in range(y)]
    for i in range(k):
        a,b = map(int,input().split())
        land[b][a] = 1
    delta = [(-1,0),(1,0),(0,1),(0,-1)]
    visited = [list(False for i in range(x)) for i in range(y)]
    stack = []
    cnt = 0
    for r in range(y):
        for c in range(x):
            if land[r][c] == 1 and visited[r][c] == False:
                visited[r][c] = True
                stack.append((r,c))
                while stack:
                    r1,c1 = stack.pop()
                    for d in delta:
                        dy = r1+d[0]
                        dx = c1+d[1]
                        if 0<=dy<y and 0<=dx<x and land[dy][dx] == 1 and visited[dy][dx] == False:
                            visited[dy][dx] = True
                            stack.append((dy,dx))
                cnt+=1
    print(cnt)