import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int,input().split())) for i in range(n)]

minus = 0
zero = 0
plus = 0
def find(x,y,z,w):
    global minus,zero,plus
    k = paper[x][z]
    for i in range(x,y):
        for j in range(z,w):
            if paper[i][j] != k:
                find(x,x+(y-x)//3,z,z+(w-z)//3)
                find(x,x+(y-x)//3,z+(w-z)//3,z+((w-z)//3)*2)
                find(x,x+(y-x)//3,z+((w-z)//3)*2,w)
                find(x+(y-x)//3,x+((y-x)//3)*2,z,z+(w-z)//3)
                find(x+(y-x)//3,x+((y-x)//3)*2,z+(w-z)//3,z+((w-z)//3)*2)
                find(x+(y-x)//3,x+((y-x)//3)*2,z+((w-z)//3)*2,w)
                find(x+((y-x)//3)*2,y,z,z+(w-z)//3)
                find(x+((y-x)//3)*2,y,z+(w-z)//3,z+((w-z)//3)*2)
                find(x+((y-x)//3)*2,y,z+((w-z)//3)*2,w)
                return
    else:
        if k == -1:
            minus+=1
        elif k == 0:
            zero+=1
        else:
            plus+=1
        return

find(0,n,0,n)
print(minus,zero,plus,sep='\n')