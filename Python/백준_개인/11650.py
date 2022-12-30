from sys import stdin
input = stdin.readline

n = int(input())
ls = []
for _ in range(n):
    x,y = map(int,input().split())
    ls.append([x,y])

ls.sort()
for i in ls:
    print(*i,sep=' ')    