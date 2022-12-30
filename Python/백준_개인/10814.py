import sys
input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    age, name = input().split()
    ls.append([int(age),_,name])
ls.sort()
for l,s,i in ls:
    print(l,i)