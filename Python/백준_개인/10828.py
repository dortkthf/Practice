import sys
input = sys.stdin.readline

n = int(input())

stacks = []

for _ in range(n):
    a = list(input().split())
    if a[0] == 'push':
        stacks.append(int(a[1]))
    elif a[0] == 'top':
        if len(stacks) != 0:
            print(stacks[-1])
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(stacks))
    elif a[0] == 'empty':
        if len(stacks) != 0:
            print(0)
        else:
            print(1)
    elif a[0] == 'pop':
        if len(stacks) != 0:
            print(stacks.pop())
        else:
            print(-1)
