from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
queue = deque(range(1,n+1))
nums = list(map(int,input().split()))

cnt = 0
ans = 0
while cnt < m:
    if queue[0] == nums[cnt]:
        queue.popleft()
        cnt+=1
    else:
        if queue.index(nums[cnt])+1 > len(queue) - (queue.index(nums[cnt])):
            queue = [queue.pop()]+list(queue)
            queue = deque(queue)
            ans+=1
        else:
            queue.append(queue.popleft())
            ans+=1
print(ans)