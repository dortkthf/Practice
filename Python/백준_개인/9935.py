import sys
input = sys.stdin.readline

word = input().rstrip()
bomb = list(input().rstrip())
word_len = len(word)
bomb_len = len(bomb)
stack = []
for i in word:
    stack.append(i)
    ls = len(stack)
    if ls >= bomb_len and stack[ls-bomb_len:] == bomb:
        for i in range(bomb_len):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(*stack,sep='')