from collections import deque
import sys
input = sys.stdin.readline

res = deque()
n = int(input())
for _ in range(n):
    cmd = list(input().split())
    if cmd[0] == 'push_back':
        res.append(int(cmd[1]))
    elif cmd[0] == 'push_front':
        res = [int(cmd[1])] + list(res)
        res = deque(res)
    elif cmd[0] == 'front':
        if len(res) == 0:
            print(-1)
            continue
        print(res[0])
    elif cmd[0] == 'back':
        if len(res) == 0:
            print(-1)
            continue
        print(res[-1])
    elif cmd[0] == 'size':
        print(len(res))
    elif cmd[0] == 'empty':
        if len(res) == 0:
            print(1)
            continue
        print(0)
    elif cmd[0] == 'pop_front':
        if len(res) == 0:
            print(-1)
            continue
        print(res.popleft())
    elif cmd[0] == 'pop_back':
        if len(res) == 0:
            print(-1)
            continue
        print(res.pop())