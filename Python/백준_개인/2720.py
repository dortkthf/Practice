import sys
input = sys.stdin.readline

t = int(input())

change = [25,10,5,1]

for _ in range(t):
    n = int(input())
    res = []
    for i in change:
        res.append(n//i)
        n %= i
    print(*res)