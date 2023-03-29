from collections import deque

n,k = map(int,input().split())
a = list(map(int,input().split()))

cnt = 0

def sort(left,right):
    global cnt
    if left == right:
        tmp = deque()
        tmp.append(a[left])
        return tmp
    mid = (left+right)//2
    tmp = deque()
    c = sort(left,mid)
    d = sort(mid+1,right)
    while len(c) > 0 or len(d) > 0:
        if len(c) == 0:
            tmp.append(d.popleft())
            cnt+=1
        elif len(d) == 0:
            tmp.append(c.popleft())
            cnt+=1
        elif c[0] > d[0]:
            tmp.append(d.popleft())
            cnt+=1
        elif c[0] < d[0]:
            tmp.append(c.popleft())
            cnt+=1
        if cnt == k:
            print(tmp[-1])
            exit(0)
    return tmp

sort(0,n-1)
print(-1)