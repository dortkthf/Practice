import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

stack = []
res = [0 for i in range(n)]
cnt = 0
for i in range(n):
    if i == 0:
        stack.append(i)
        cnt+=1
    elif a[i] > a[stack[-1]]:
        while True:
            res[stack.pop()] = a[i]
            cnt-=1
            if cnt == 0 or a[i] <= a[stack[-1]]:
                break
        stack.append(i)
        cnt+=1
    else:
        stack.append(i)
        cnt+=1
for i in stack:
    res[i] = -1

print(*res)