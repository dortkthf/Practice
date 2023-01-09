n = int(input())

chess = [list(0 for i in range(n)) for i in range(n)]


d = [[-1,-1],[-1,1],[1,1],[1,-1],[-1,0],[1,0],[0,1],[0,-1]]

def cross(x,y):
    chess[x][y] = 1 
    rx,ry = x,y
    for i in d:
        x,y = rx,ry
        while x+i[0] < n and y+i[1] < n and x+i[0] >=0 and y+i[1] >= 0:
            chess[x+i[0]][y+i[1]] = 1
            x = x+i[0]
            y = y+i[1]

def decross(x,y):
    chess[x][y] = 0 
    rx,ry = x,y
    for i in d:
        x,y = rx,ry
        while x+i[0] < n and y+i[1] < n and x+i[0] >=0 and y+i[1] >= 0:
            chess[x+i[0]][y+i[1]] = 0
            x = x+i[0]
            y = y+i[1]
res = 0
cnt = 0
def queen():
    global cnt, res
    for i in range(n):
        for j in range(n):
            if cnt == n:
                res+=1
                return
            if chess[i][j] == 0:
                cnt+=1
                cross(i,j)
                queen()
                decross(i,j)
                cnt-=1

queen()
print(res)
