data = [list(map(int,input().split())) for i in range(19)]
n = int(input())
for i in range(n) :
    x, y = map(int,input().split())
    for i in range(19) :
        if data[i][y-1] == 0 :
            data[i][y-1] =1
        else :
            data[i][y-1] =0
    for i in range(19) :
        if data[x-1][i] == 0:
            data[x-1][i] =1
        else :
            data[x-1][i] =0
for i in range(19) :
    for j in range(19) :
        print(data[i][j], end=' ')
    print()