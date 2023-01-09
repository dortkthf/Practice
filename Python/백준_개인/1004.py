import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x1,y1,x2,y2 = map(int,input().split())
    cnt = 0
    n = int(input())
    for _ in range(n):
        x,y,r = map(int,input().split())
        # 방법 1
        # if ((x-x1)**2+(y-y1)**2) < r**2 and ((x-x2)**2+(y-y2)**2) < r**2:
        #     pass
        # elif (((x-x1)**2+(y-y1)**2) < r**2 and ((x-x2)**2+(y-y2)**2) > r**2) or (((x-x1)**2+(y-y1)**2) > r**2 and ((x-x2)**2+(y-y2)**2) < r**2):
        #     cnt+=1
        # 방법 2
        res1 = ((x-x1)**2+(y-y1)**2) - r**2
        res2 = ((x-x2)**2+(y-y2)**2) - r**2
        if res1*res2 < 0:
            cnt+=1
    print(cnt)