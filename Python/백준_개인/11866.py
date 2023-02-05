import sys, copy
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(range(1,n+1))

n2 = copy.copy(n)
k2 = copy.copy(k)
res = []
if n == 1:
    print('<1>')
    exit(0)
for i in range(n):
    if i == 0:
        k2 = k-1
        res+=['<'+str(nums[k2])]
        nums.remove(nums[k2])
        n2-=1
    elif i == n-1:
        res+=[str(nums[0])+'>']
    else:
        k2 += k-1
        if k2>=n2:
            k2%=n2
            res+=[nums[k2]]
            nums.remove(nums[k2])
            n2-=1
        else:
            res+=[nums[k2]]
            nums.remove(nums[k2])
            n2-=1
print(*res,sep=', ')