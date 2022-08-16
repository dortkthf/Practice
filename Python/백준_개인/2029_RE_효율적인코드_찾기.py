graph = [list(input()) for i in range(10)]
cnt = 0
square = 0
delta1 = [(0,1),(1,0)]
delta2 = [(0,-1),(-1,0)]
for y in range(10):
    for x in range(10):
        if graph[y][x] == '+':
            for d in delta1:
                dy = y+d[0]
                dx = x+d[1]
                if 0<=dy<10 and 0<=dx<10:
                    if graph[dy][dx] == '.':
                        cnt+=1

for y in range(10):
    for x in range(10):
        tmp = 0
        if graph[y][x] == '+':
            for d in delta1:
                dy = y+d[0]
                dx = x+d[1]
                if 0<=dy<10 and 0<=dx<10:
                    if graph[dy][dx] == '|' or graph[dy][dx] == '-':
                        tmp+=1
            if tmp == 2:
                x1 = x+3
                y1 = y+3
                for d in delta2:
                    dy = y1+d[0]
                    dx = x1+d[1]
                    if 0<=dy<10 and 0<=dx<10:
                        if graph[dy][dx] == '|' or graph[dy][dx] == '-':
                            tmp+=1
            if tmp == 4:
                square+=1
                continue

for y in range(4):
    for x in range(4):
        if graph[y][x] == '+':
            tmp = 0
            for d in delta1:
                dy = y+d[0]
                dx = x+d[1]
                if 0<=dy<10 and 0<=dx<10:
                    if graph[dy][dx] == '|' and graph[dy+3][dx] == '|':
                        tmp+=1
                    if graph[dy][dx] == '-' and graph[dy][dx+3] == '-':
                        tmp+=1
                if tmp == 2:
                    x1 = x+6
                    y1 = y+6
                    for d in delta2:
                        dy = y1+d[0]
                        dx = x1+d[1]
                        if 0<=dy<10 and 0<=dx<10:
                            if graph[dy][dx] == '|' and graph[dy-3][dx] == '|':
                                tmp+=1
                            if graph[dy][dx] == '-' and graph[dy][dx-3] == '-':
                                tmp+=1
                if tmp == 4:
                    square+=1
                    continue

for y in range(1):
    for x in range(1):
        if graph[y][x] == '+':
            tmp = 0
            for d in delta1:
                dy = y + d[0]
                dx = x + d[1]
                if graph[dy][dx] == '|' and graph[dy+3][dx] == '|' and graph[dy+6][dx] == '|':
                    tmp+=1
                if graph[dy][dx] == '-' and graph[dy][dx+3] == '-' and graph[dy][dx+6] == '-':
                    tmp+=1
                if tmp == 2:
                    y1 = y+9
                    x1 = x+9
                    for d in delta2:
                        dy = y1 + d[0]
                        dx = x1 + d[1]
                        if graph[dy][dx] == '|' and graph[dy-3][dx] == '|' and graph[dy-6][dx] == '|':
                            tmp+=1
                        if graph[dy][dx] == '-' and graph[dy][dx-3] == '-' and graph[dy][dx-6] == '-':
                            tmp+=1
                if tmp == 4:
                    square+=1
                    continue
print(cnt, square)