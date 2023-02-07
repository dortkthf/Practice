import copy, sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def init(a,tree,node,start,end):
    if start == end:
        tree[node] = start
    else:
        mid = (start+end)//2
        init(a,tree, node*2, start, mid)
        init(a, tree, node*2+1, mid+1,end)
        if nums[tree[node*2]] > nums[tree[node*2+1]]:
            tree[node] = tree[node*2+1]
        else:
            tree[node] = tree[node*2]

def query(tree,node,start,end,left,right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    l = query(tree,node*2, start, (start+end)//2, left, right)
    r = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    if l == -1:
        return r
    elif r == -1:
        return l
    else:
        if nums[l] > nums[r]:
            return r
        else:
            return l

def find(start,end,n):
    global stacks, histo, n2
    if n == 1:
        if stacks<histo[start]:
            stacks = histo[start]
        return
    idx_min = query(tree,1,0,n2-1,start,end)
    if stacks<histo[idx_min]*n:
        stacks = histo[idx_min]*n

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
    tree = [0 for i in range(2*n+2)]
    if n == 0:
        break
    else:
        histo = nums[1:n+1]
        find(0,n,n)
        print(stacks)




# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def init(a,tree,node,start,end):
#     if start == end:
#         tree[node] = start
#     else:
#         mid = (start+end)//2
#         init(a,tree, node*2, start, mid)
#         init(a, tree, node*2+1, mid+1,end)
#         if nums[tree[node*2]] > nums[tree[node*2+1]]:
#             tree[node] = tree[node*2+1]
#         else:
#             tree[node] = tree[node*2]

# def query(tree,node,start,end,left,right):
#     if left > end or right < start:
#         return -1
#     if left <= start and end <= right:
#         return tree[node]
#     l = query(tree,node*2, start, (start+end)//2, left, right)
#     r = query(tree, node*2+1, (start+end)//2+1, end, left, right)
#     if l == -1:
#         return r
#     elif r == -1:
#         return l
#     else:
#         if nums[l] > nums[r]:
#             return r
#         else:
#             return l

# def find(s,e,n):
#     global stack
#     if n == 1:
#         if stack < nums[s]:
#             stack = nums[s]
#         return
#     sm_idx = query(tree,1,0,n2-1,s,e-1)
#     if nums[sm_idx]*n > stack:
#         stack = nums[sm_idx]*n
#     if s == sm_idx:
#         find(s+1,e,n-1)
#         return
#     elif e-1 == sm_idx:
#         find(s,sm_idx,n-1)
#         return
#     find(s,sm_idx,sm_idx-s)
#     find(sm_idx+1,e,e-sm_idx-1)
#     return

# while True:
#     nums = list(map(int,input().split()))
#     n = nums[0]
#     if n == 0:
#         break
#     n2 = n
#     tree = [0 for i in range(3*n)]

#     stack = 0
#     init(nums,tree,1,0,n-1)
#     find(0,n,n)
#     print(stack)