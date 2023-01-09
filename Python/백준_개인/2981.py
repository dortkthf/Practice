
# 기본 사고방식 : a 와 b 가 m 으로 나눈 나머지가 동일하면 a-b는 m 의 배수이다
# a, b, c, d, e, f 도 m으로 나눈 나머지가 동일 하다면 a-b도 b-c도 c-d도 m의 배수이다 고로 a-b의 공약수와 b-c 의 공약수를 구하고
# 나온 값의 공약수와 c-d의 공약수도 구하고 이런식으로 진행하면 된다.

# 1. 무작정 풀어보기

import sys, math
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for i in range(n)]
nums.sort()

nums2 = []

res = []

for i in range(n-1):
    nums2.append(nums[i+1]-nums[i])

for i in nums2:
    nums3 = [] 
    for j in range(1,int(i**(1/2))+1):
        if i%j == 0:
            nums3.append(j)
            nums3.append(i//j)
    nums3.sort()
    for k in nums3:
        for a in nums:
            if nums.index(a) == 0:
                tmp = a%k
            if a%k != tmp:
                break
        else:
            res.append(k)
res = list(set(res))
res.sort()
res.remove(1)
print(*res, sep=' ')


# 2. 가장 현명한 풀이 

import sys, math
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for i in range(n)]
nums.sort()
gcd = nums[1] - nums[0]
res = []
for i in range(n-1):
    gcd = math.gcd(gcd,nums[i+1]-nums[i])
for i in range(1,int(math.sqrt(gcd))+1):
    if gcd%i == 0:
        res.append(i)
        res.append(gcd//i)
res = list(set(res))
res.sort()
res.remove(1)
print(*res, sep=' ')