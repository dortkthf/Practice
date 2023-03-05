# 1. 이분탐색 직접구현해서 풀기
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
dp = [0,a[0]] + list(0 for i in range(n-1))
current = 1

def bs(left,right,value):
    mid = (left+right)//2

    if value > dp[right]:
        return -1
    if right-left == 1:
        if dp[left] < value and value <= dp[right]:
            return right
    if value > dp[mid]:
        return bs(mid,right,value)
    if value <= dp[mid]:
        return bs(left,mid,value)

for i in range(1,n):
    index = bs(0,current,a[i])
    if index == -1:
        current+=1
        dp[current] = a[i]
    else:
        dp[index] = a[i]

print(current)

# 2. python bisect 함수 사용해서 풀기 직접구현 X
# import sys, bisect
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int,input().split()))
# res = [a[0]]

# for num in a:
#     if res[-1] < num:
#         res.append(num)
#         continue
#     index = bisect.bisect_left(res,num)
#     res[index] = num

# print(len(res))