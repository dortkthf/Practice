import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n,m,r = map(int,input().split())

graph = list([] for i in range(n+1))
check = [0 for i in range(n+1)]

check[r] = 1

cnt = 1

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort(reverse=True)

def find(x):
    global cnt
    for i in graph[x]:
        if check[i] == 0:
            cnt+=1
            check[i] = cnt
            find(i)
    else:
        return
    
find(r)

for i in range(1,n+1):
    print(check[i])