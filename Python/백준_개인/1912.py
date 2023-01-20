import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))

sol = []
for i in range(n):
    if i == 0:
        res = numbers[i]
    elif res<0:
        res = numbers[i]
    else:
        res=numbers[i]+res
    sol.append(res)
print(max(sol))