from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    r = 0
    error = False
    p = input()
    n = int(input())
    lst = input().rstrip().strip('[').strip(']')
    if len(lst) == 0:
        lst = deque()
    else:
        lst = deque(lst.split(','))
    for i in p:
        if i == 'R':
            r+=1
        elif i == 'D':
            if len(lst) == 0:
                error = True
                break
            elif r%2 == 0:
                lst.popleft()
            elif r%2 == 1:
                lst.pop()
    if error:
        print('error')
        continue
    if r%2 == 0:
        print('['+','.join(list(lst))+']')
    else:
        print('['+','.join(list(lst)[::-1])+']')