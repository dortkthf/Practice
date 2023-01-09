k = int(input())
cnt = [0 for i in range(5)]
res = [[] for i in range(7)]
res2 = []
ckc = []
nm = 1

for i in range(6):
    x,y = map(int,input().split())
    cnt[x] += 1
    res[x].append(y)
    res2.append([x,y])
for i in range(5):
    if cnt[i] == 1:
        nm*=res[i][0]
        ckc.append(i)

tmp = []
tmp2 = []
ctmp = 0
for i in res2:
    if i[0] not in ckc:
        tmp.append(i[1])
    else:
        ctmp += 1
        if ctmp == 2:
            tmp2 = tmp
            tmp = []
tmp3 = tmp+tmp2

nm = nm-(tmp3[1]*tmp3[2])
print(nm*k)
