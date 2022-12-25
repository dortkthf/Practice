n,m = map(int,input().split())
list1 = [list(map(int,input().split())) for i in range(n)]
list2 = [list(map(int,input().split())) for i in range(n)]

res = [list(0 for i in range(m)) for i in range(n)]
for i in range(n):
    for j in range(m):
        res[i][j]=list1[i][j]+list2[i][j]
for i in res:
    print(*i)