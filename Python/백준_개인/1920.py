import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
n_nums = list(map(int,input().split()))
n_nums.sort()
m = int(input())
m_nums = list(map(int,input().split()))


def find(x,start,end):
    global res
    if end-start == 1:
        if x == n_nums[start] or x == n_nums[end]:
            res = True
        return
    elif x > n_nums[start+(end-start)//2]:
        find(x,start+(end-start)//2,end)
        return
    elif x < n_nums[start+(end-start)//2]:
        find(x,start,start+(end-start)//2)
        return
    elif x == n_nums[start+(end-start)//2]:
        res = True
        return

for i in m_nums:
    if n == 1:
        if i == n_nums[0]:
            print(1)
        else:
            print(0)
        continue
    res = False
    find(i,0,n-1)
    if res == True:
        print(1)
    else:
        print(0)   