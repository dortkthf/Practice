import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def init(node,start,end):
    global tree
    if start == end:
        tree[node] = start
        return tree[node]
    mid = (start+end)//2
    a = init(2*node, start,mid)
    b = init(2*node+1,mid+1,end)
    if nums[a] > nums[b]:
        tree[node] = b
        return tree[node]
    else:
        tree[node] = a
        return tree[node]

def query(node,start,end,x,y):
    mid = (start+end)//2
    if start > y or end < x:
        return inf*10
    if x <= start and end <= y:
        return tree[node]

    a = query(2*node,start,mid,x,y)
    b = query(2*node+1,mid+1,end,x,y)
    if a == inf*10:
        return b
    elif b == inf*10:
        return a
    elif nums[a] > nums[b]:
        return b
    else:
        return a

def find(start,end):
    global res
    if start == end:
        if res < nums[start]:
            res = nums[start]
        return
    idx = query(1,0,n-1,start,end)
    if res < nums[idx]*(end+1-start):
        res = nums[idx]*(end+1-start)
    if idx == start:
        find(idx+1,end)
        return
    if idx == end:
        find(start,end-1)
        return
    find(start,idx-1)
    find(idx+1,end)
    return

while True:
    nums = list(map(int,input().split()))
    n = nums[0]
    if n == 0:
        break
    nums = nums[1:]
    res = 0
    inf = 101**10
    tree = [0 for i in range(4*n)]
    init(1,0,n-1)
    find(0,n-1)
    print(res)