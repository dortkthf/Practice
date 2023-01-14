import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = [0,1,1,1,2,2] + [0 for i in range(95)]
    n = int(input())
    if n<6:
        print(p[n])
        continue
    for i in range(6,n+1):
        p[i] = p[i-1] + p[i-5]
    print(p[n])