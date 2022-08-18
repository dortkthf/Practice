n = int(input())
maps = [list(map(int,input())) for i in range(n)]
visited = [[False for i in range(n)] for i in range(n)]
stack = []
house_nums = []
delta = [(-1,0),(1,0),(0,1),(0,-1)]
cnt = 0
for y in range(n):
    for x in range(n):
        tmp = 0
        if maps[y][x] == 1 and visited[y][x] == False:
            visited[y][x] = True
            tmp+=1
            stack.append((y,x))
            while stack:
                y1,x1 = stack.pop()
                for d in delta:
                    dy = y1+d[0]
                    dx = x1+d[1]
                    if 0<=dy<n and 0<=dx<n and maps[dy][dx] == 1 and visited[dy][dx] == False:
                        stack.append((dy,dx))
                        visited[dy][dx] = True
                        tmp+=1
            house_nums.append(tmp)
            cnt+=1
print(cnt)
house_nums.sort()
print(*house_nums,sep='\n')

