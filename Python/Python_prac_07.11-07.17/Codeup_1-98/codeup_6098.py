data = [list(map(int,input().split())) for i in range(10)]
data[1][1]=9
x,y = 1,1
data[1][1]=9
while True:
    if data[x][y+1] == 0:
        data[x][y+1] =9
        y+=1
        continue
    elif data[x][y+1] == 1 and data[x+1][y] == 0:
        data[x+1][y] =9
        x+=1
        continue
    elif data[x][y+1] == 2:
        data[x][y+1] =9
        break
    elif data[x+1][y] ==2:
        data[x+1][y] =9
        break
    else:
        break
for i in range(10):
    for j in range(10):
        print(data[i][j],end=' ')
    print()
        