n = input()
res = []
for i in n:
    res.append(int(i))
res.sort(reverse=True)
print(*res,sep='')