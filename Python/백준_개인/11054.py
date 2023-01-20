n = int(input())
a = list(map(int,input().split()))
ma = a[::-1]

plus = [1 for i in range(n)]
minus = [1 for i in range(n)]
res = [ 0 for i in range(n)]

for i in range(1,n):
    for j in range(i):
        if a[j] < a[i]:
            plus[i] = max(plus[i], plus[j]+1)
    for k in range(i):
        if ma[k] < ma[i]:
            minus[i] = max(minus[i], minus[k]+1)

minus.reverse()

for i in range(n):
    res[i] = plus[i]+minus[i]

print(max(res)-1)