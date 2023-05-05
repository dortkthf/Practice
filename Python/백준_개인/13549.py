from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
check = list(0 for i in range(100001))
queue = deque()
queue.append((n,0))
check[n] = 1

def find(n,k):
    if n >= k:
        return n-k
    
    while queue:
        loc,time = queue.popleft()
        if loc == k:
            return time
        
        for i in (loc*2,loc-1,loc+1):
            if 0<=i<=100000 and check[i] == 0:
                check[i] = 1
                new_time = time if i == loc*2 else time+1
                queue.append((i,new_time))
print(find(n,k))