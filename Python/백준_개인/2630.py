n = int(input())
cft = [list(map(int,input().split())) for i in range(n)]

blue = 0
white = 0
def find(x,y,z,w):
    k = cft[x][z]
    global blue, white
    for i in range(x,y):
        for j in range(z,w):
            if cft[i][j] != k:
                find(x,x+(y-x)//2,z,z+(w-z)//2)
                find(x,x+(y-x)//2,z+(w-z)//2,w)
                find(x+(y-x)//2,y,z,z+(w-z)//2)
                find(x+(y-x)//2,y,z+(w-z)//2,w)
                return
    else:
        if k == 1:
            blue+=1
            return
        white+=1
        return

find(0,n,0,n)
print(white,blue,sep='\n')