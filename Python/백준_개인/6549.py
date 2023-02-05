import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(start,end,n):
    global stacks, nums, n2
    if n == 1:
        stacks.append(nums[start])
        return
    elif n != n2:
        idx_min = nums[start:end].index(min(nums[start:end]))+start
        if idx_min == start:
            stacks.append(nums[idx_min]*n)
            find(start+1,end,end-start-1)
            return
        elif idx_min+1 == end:
            stacks.append(nums[idx_min]*n)
            find(start,idx_min,idx_min-start)
            return
    else:
        idx_min = nums.index(min(nums[start:end]))
        if idx_min == start:
            stacks.append(nums[idx_min]*n)
            find(start+1,end,end-start-1)
            return
        elif idx_min+1 == end:
            stacks.append(nums[idx_min]*n)
            find(start,idx_min,idx_min-start)
            return

    find(start,idx_min,idx_min-start)
    find(idx_min+1,end,end-idx_min-1)
    return

while True:
    stacks = []
    nums = list(map(int,input().split()))[1:]
    n = len(nums)
    n2 = n
    if n == 0:
        break
    find(0,n,n)
    print(max(stacks))
