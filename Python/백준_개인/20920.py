import sys
input = sys.stdin.readline

n,m = map(int,input().split())

res = [[] for i in range(n+1)]
dic = {}

for i in range(n):
    word = input().rstrip()
    wl = len(word)
    if wl >= m:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

for i in dic:
    res[dic[i]].append(i)

for i in res:
    if i:
        i.sort(key=lambda x : (-len(x),x))

res.reverse()

for i in res:
    if i:
        print(*i,sep='\n')