n = int(input())
video = [input() for i in range(n)]

res = ''
def cmps(x,y,z,w):
    global res
    k = video[x][z]
    for i in range(x,y):
        for j in range(z,w):
            if video[i][j] != k:
                res=res+'('
                cmps(x,x+(y-x)//2,z,z+(w-z)//2)
                cmps(x,x+(y-x)//2,z+(w-z)//2,w)
                cmps(x+(y-x)//2,y,z,z+(w-z)//2)
                cmps(x+(y-x)//2,y,z+(w-z)//2,w)
                res=res+')'
                return
    else:
        if k == '0':
            res=res+'0'
            return
        res=res+'1'
        return
cmps(0,n,0,n)
print(res)