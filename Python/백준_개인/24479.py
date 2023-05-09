import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n,m,r = map(int,input().split())

graph = list([] for i in range(n+1))

cnt = 1
check = {r:1}

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

def find(x):
    global cnt
    for i in graph[x]:
        if i not in check:
            cnt+=1
            check[i] = cnt
            find(i)
    else:
        return

find(r)
for i in range(1,n+1):
    if i not in check:
        check[i] = 0

check = sorted(check.items())

for k,v in check:
    print(v)