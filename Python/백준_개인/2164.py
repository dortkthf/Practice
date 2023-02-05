from collections import deque
import sys, copy
input = sys.stdin.readline

n = int(input())

queue = deque(range(1,n+1))
n2 = copy.copy(n)

for i in range(n):
    if n2 == 1:
        print(queue[0])
        break
    queue.popleft()
    n2-=1
    queue.append(queue.popleft())