import sys
input = sys.stdin.readline

from collections import deque

n,k = map(int,input().split())

queue = deque()
queue.append((n,0))

check = list(0 for i in range(100001))
check[n] = 1

while queue:
    x,time = queue.popleft()

    if x == k:
        print(time)
        break
    
    for next_x in ((x-1),(x+1)):
        if 0 <= next_x <= 100000 and check[next_x] == 0:
            queue.append((next_x, time+1))
            check[next_x] = 1
            
    next_x = x*2
    if 0 <= next_x <= 100000 and check[next_x] == 0:
        queue.append((next_x,time+1))
        check[next_x] = 1