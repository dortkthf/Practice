import sys, heapq
input = sys.stdin.readline

N,E = map(int,input().split())
graph = [[] for i in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
v1,v2 = map(int,input().split())
if v1 > v2:
    fst = v2
    scd = v1
else:
    fst = v1
    scd = v2
    
def find(X):
    queue = [(0,X)]
    distances = [sys.maxsize for i in range(1+N)]
    distances[X] = 0
    while queue:
        current_distance,current_vertex = heapq.heappop(queue)
        for vertex,distance in graph[current_vertex]:
            new_distance = current_distance+distance
            if distances[vertex] > new_distance:
                distances[vertex] = new_distance
                heapq.heappush(queue,(new_distance,vertex))
    return distances

distances_1 = find(1)
distances_fst = find(fst)
distances_scd = find(scd)

result = (min(distances_1[fst]+distances_fst[scd]+distances_scd[N],distances_1[scd]+distances_scd[fst]+distances_fst[N]))
if result<sys.maxsize:
    print(result)
else:
    print(-1)