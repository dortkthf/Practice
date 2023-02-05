from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    prior = deque(map(int,input().split()))
    nums = deque(range(n))
    res = []
    if n == 1:
        print(1)
        continue
    while True:
        if len(prior) == 0:
            break
        if prior[0] < max(prior):
            prior.append(prior.popleft())
            nums.append(nums.popleft())
        else:
            prior.popleft()
            res.append(nums.popleft())
    print(res.index(m)+1)