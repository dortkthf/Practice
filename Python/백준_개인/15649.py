from itertools import permutations

n, m = map(int, input().split())

nlist = sorted(list(i for i in range(1,n+1)))
perm = list(permutations(nlist, m))
for i in perm:
    print(*i,sep=' ')
