from collections import deque
import sys
input = sys.stdin.readline

k = int(input())

for _ in range(k):
    V,E = map(int,input().split())
    graph = list([] for i in range(V+1))
    check = list(0 for i in range(V+1))
    queue = deque()
    res = 'YES'
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    def binary_graph(V):
        for i in range(1,V+1):
            if check[i] == 0:
                check[i] = 1
                queue.append(i)
                while queue:
                    num = queue.popleft()
                    for j in graph[num]:
                        if check[j] == 0:
                            check[j] = 3 - check[num]
                            queue.append(j)
                        elif check[j] == check[num]:
                            return 'NO'
        return 'YES'
    print(binary_graph(V))