import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int,input().split())

graph = list([] for i in range(n+1))
c_dfs = [0 for i in range(n+1)]
c_bfs = [0 for i in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfsres = [v]
c_dfs[v] = 1

def find(x):
    for i in graph[x]:
        if c_dfs[i] == 0:
            c_dfs[i] = 1
            dfsres.append(i)
            find(i)
    else:
        return
    
find(v)
print(*dfsres)

bfsres = [v]
queue = deque()
queue.append(v)
c_bfs[v] = 1
while queue:
    for i in graph[queue[0]]:
        if c_bfs[i] == 0:
            queue.append(i)
            bfsres.append(i)
            c_bfs[i] = 1
    queue.popleft()

print(*bfsres)