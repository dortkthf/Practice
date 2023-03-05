import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    word = input().rstrip()
    print(word[0],word[-1],sep='')