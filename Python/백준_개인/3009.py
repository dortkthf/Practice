import sys
input = sys.stdin.readline

dic1 = {}
dic2 = {}
for i in range(3):
    x,y = map(int,input().split())
    if x in dic1:
        dic1[x] += 1
    else:
        dic1[x] = 1
    
    if y in dic2:
        dic2[y] += 1
    else:
        dic2[y] = 1

res = []
for k,v in dic1.items():
    if v == 1:
        res.append(k)

for k,v in dic2.items():
    if v == 1:
        res.append(k)

print(*res, sep=' ')