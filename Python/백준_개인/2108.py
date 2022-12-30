from sys import stdin
input = stdin.readline

n = int(input())
ls = [int(input()) for _ in range(n)]
ls.sort()
print(round(sum(ls)/len(ls)))
print(ls[len(ls)//2])
res = {}
rmax = []
for i in ls:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1
for i in res.values():
    rmax.append(i)
realmax = max(rmax)
ans = []
for i,v in res.items():
    if v == realmax:
        ans.append(i)
if len(ans)>1:
    print(ans[1])
else:
    print(ans[0])
print(max(ls)-min(ls))