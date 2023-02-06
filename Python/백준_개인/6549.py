import copy, sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def init(node,s,e):
    global seg, nums
    if s == e:
        seg[node] = [nums[s],s]
        return seg[node]
    mid = (s+e)//2
    seg[node] = [min(init(2*node,s,mid)[0],init(2*node+1,mid+1,e)[0])]
    if seg[node][0] == init(2*node,s,mid)[0]:
        seg[node].append(init(2*node,s,mid)[1])
    else:
        seg[node].append(init(2*node+1,mid+1,e)[1])
    return seg[node]

def query(node,s,e,l,r):
    global seg
    if e<l or r<s:
        return inf
    if l<=s and e<=r:
        return seg[node]
    mid = (s+e)//2
    seg[node].append(min(query(2*node,s,mid,l,r)[0], query(2*node+1,mid+1,e,l,r)[0]))    
    if seg[node][0] == query(2*node,s,mid,l,r)[0]:
        seg[node].append(query(2*node,s,mid,l,r)[1])
    else:
        seg[node].append(query(2*node+1,mid+1,e,l,r)[1])
    return seg[node]

def find(start,end,n):
    global stacks, nums, n2
    if n == 1:
        if stacks<nums[start]:
            stacks = nums[start]
        return
    elif n != n2:
        idx_min = query(1,1,7,start,end-1)[1]
    else:
        idx_min = query(1,1,7,start,end-1)[1]
    
    if stacks<nums[idx_min]*n:
        stacks = nums[idx_min]*n

    if idx_min == start:   
        find(start+1,end,end-start-1)
        return
    elif idx_min+1 == end:
        find(start,idx_min,idx_min-start)
        return
    find(start,idx_min,idx_min-start)
    find(idx_min+1,end,end-idx_min-1)
    return

while True:
    stacks = 0
    nums = list(map(int,input().split()))
    n = nums[0]
    n2 = n
    inf = 10**6
    del nums[0]
    seg = [[] for i in range(2*n)]

    if n == 0:
        break
    init(1,0,n-1)
    # find(0,n,n)
    print(seg)
    print(stacks)