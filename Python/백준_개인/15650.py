from itertools import combinations

n,m = map(int,input().split())

nl = list(i for i in range(1,n+1))
cmb = list(combinations(nl,m))

for i in cmb:
    print(*i)