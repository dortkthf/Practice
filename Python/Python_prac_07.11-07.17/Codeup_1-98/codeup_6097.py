h,w = map(int,input().split())
data = []
for i in range(h) :
    data.append([])
    for j in range(w) :
        data[i].append(0)
n = int(input())

for i in range(n):
    l,d,x,y = map(int,input().split())
    if d == 0 :
        for i in range(l):
            data[x-1][y-1+i] = 1
    else :
        for i in range(l) :
            data[x-1+i][y-1] = 1
for i in range(h) :
    for j in range(w):
        print(data[i][j],end=' ')
    print()