# sys는 시간초과시에 사용한다
from sys import stdin
input = stdin.readline

n = int(input())
ls = [0 for i in range(10001)]

for i in range(n):
    ls[int(input())] += 1

for i in range(10001):
    if ls[i] != 0:
        for j in range(ls[i]):
            print(i)