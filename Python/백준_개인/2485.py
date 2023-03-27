import sys, math
input = sys.stdin.readline

n = int(input())
res = list()

tmp = 0
tmp2 = 0
for i in range(n):
    if i == 0:
        tmp = int(input())
    else:
        tmp2 = int(input())
        res.append(tmp2-tmp)
        tmp = tmp2

res2 = list(set(res))

a = 0
for i in range(len(res2)-1):
    if i == 0:
        a = math.gcd(res2[i],res2[i+1])
    else:
        a = math.gcd(a,res2[i+1])

cnt = 0
if a == 0:
    print(0)
    exit(0)

for i in res:
    cnt+=(i//a)-1

print(cnt)