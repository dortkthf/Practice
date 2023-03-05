import sys
input = sys.stdin.readline

n,c = map(int,input().split())
house = list(int(input()) for i in range(n))
house.sort()

if house[0] == house[-1]:
    print(0)
    exit(0)
elif c == 2:
    print(house[-1]-house[0])
    exit(0)
def func(x):
    idx = 0
    cnt = 0
    for i in range(n):
        if i == 0:
            idx = house[i]
            cnt+=1
            continue
        if idx + x <= house[i]:
            idx = house[i]
            cnt+=1
    return cnt

def find(start,end):
    mid = (start+end)//2
    if end-start == 1:
        if func(end) == c:
            print(end)
            exit(0)
        print(start)
        exit(0)
    
    end_cnt = func(end)
    mid_cnt = func(mid)

    if end_cnt<=c and mid_cnt>=c:
        find(mid,end)
        return
    start_cnt = func(start)
    if mid_cnt<=c and start_cnt>=c:
        find(start,mid)
        return
find(0,house[-1])