# 부분합들의 나머지가 같은것들 중에서 2개를 고르는 방법을 구하면된다.
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))

res = [0 for i in range(m)]
cnt = 0
ans = 0
for i in nums:
    cnt+=i
    res[cnt%m] += 1

ans += res[0]

for i in res:
    if i != 0:
        ans += i*(i-1)//2

print(ans)