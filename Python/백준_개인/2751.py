import sys
n = int(sys.stdin.readline())
ls = [ int(sys.stdin.readline()) for i in range(n)]
ls.sort()

for i in ls:
    print(i)
