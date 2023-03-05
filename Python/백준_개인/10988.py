import sys
input = sys.stdin.readline

word = input().rstrip()
compare = word[::-1]

if word == compare:
    print(1)
else:
    print(0)