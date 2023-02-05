import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int,input().split())) for i in range(n)]
nums.sort(key= lambda x : (x[1],x[0]))
# print(nums)
cnt = 1
s,e = nums[0]
if n == 1:
    print(cnt)
else:
    for i in range(1,n):
        if nums[i][0] >= e:
            cnt+=1
            s,e = nums[i]
    print(cnt)