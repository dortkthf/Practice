import sys
input = sys.stdin.readline

n = int(input())

for i in range(1,n+1):
    if i*(i+2) >= n:
        print(i)
        break