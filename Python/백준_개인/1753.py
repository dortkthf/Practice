import sys
import heapq
input = sys.stdin.readline

V,E = map(int,input().split())
K = int(input())

graph = [[] for i in range(1+V)]
distances = [sys.maxsize for i in range(V+1)]
distances[K] = 0
queue = [(0,K)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

while queue:
    
    distance, vertex = heapq.heappop(queue)

    for neighbor, weight in graph[vertex]:
        
        distance1= distance+weight
        
        if distances[neighbor] > distance1:
            distances[neighbor] = distance1
            heapq.heappush(queue, (distance1,neighbor))
            
for i in range(1,V+1):
    if distances[i] == sys.maxsize:
        print('INF')
        continue
    print(distances[i])