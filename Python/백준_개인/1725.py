import sys
input = sys.stdin.readline

n = int(input())

stack = []
res = 0

for i in range(n+1):
    if i == n:
        idx, number = i, 0
    else:
        idx, number = i, int(input())

    while stack and stack[-1][1] > number:
        idx, number2 = stack.pop()
        res = max(res, (i-idx)*number2)
    stack.append((idx,number))

print(res)