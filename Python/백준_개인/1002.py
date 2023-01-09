import math, sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    if max([r1,r2]) == r1:
        bx,by,br,sx,sy,sr = x1,y1,r1,x2,y2,r2
    else:
        bx,by,br,sx,sy,sr = x2,y2,r2,x1,y1,r1
    d = math.sqrt(((bx-sx)**2)+((by-sy)**2))
    # 한점에서 만날때 
    if d+sr == br or d == sr+br:
        print(1)
    # 두점에서 만날때
    elif d+sr > br and br > d-sr:
        print(2)
    # 안만날때
    else:
        print(0)