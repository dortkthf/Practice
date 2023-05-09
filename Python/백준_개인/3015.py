import sys
input = sys.stdin.readline

n = int(input())

stack = []
res = 0

for _ in range(n):
    now = int(input())
    cnt = 1

    while stack and stack[-1][0] <= now:
        top, cnt = stack.pop()
        if top < now:
            res+=cnt
            cnt=1
        elif top == now:
            res+=cnt
            cnt+=1
    
    if stack:
        res+=1

    stack.append((now,cnt))
print(res)