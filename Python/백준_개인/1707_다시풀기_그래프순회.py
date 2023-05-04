from collections import deque
import sys
input = sys.stdin.readline

k = int(input())

for _ in range(k):
    
    V,E = map(int,input().split())
    graph = list([] for i in range(V+1))
    check = [0 for i in range(V+1)]
    queue = deque()
    
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    def find(x):
        for i in range(1,x+1):
            if check[i] == 0:
                check[i] = 1
                queue.append(i)
                
                while queue:
                    k = queue.popleft()
                    for i in graph[k]:
                        if check[i] == 0:
                            check[i] = 3 - check[k]
                            queue.append(i)
                        elif check[i] == check[k]:
                            return False
        return True
    
    if find(V):
        print('YES')
    else:
        print('NO')