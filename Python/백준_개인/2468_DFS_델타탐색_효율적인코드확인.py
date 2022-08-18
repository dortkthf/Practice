n = int(input())
maps = [list(map(int,input().split())) for i in range(n)]
mxheight = max(list(max(maps[i]) for i in range(n)))
delta = [(-1,0),(1,0),(0,1),(0,-1)]
safes = []
for k in range(mxheight):
    visited = [list(False for i in range(n)) for i in range(n)]
    stack = []
    cnt = 0
    for y in range(n):
        for x in range(n):
            if maps[y][x] > k and visited[y][x] == False:
                stack.append((y,x))
                visited[y][x] = True
                while stack:
                    y1,x1 = stack.pop()
                    for d in delta:
                        dy = y1 + d[0]
                        dx = x1 + d[1]
                        if 0<=dy<n and 0<=dx<n and maps[dy][dx] >k and visited[dy][dx] == False:
                            stack.append((dy,dx))
                            visited[dy][dx] = True
                cnt+=1
    safes.append(cnt)
print(max(safes))