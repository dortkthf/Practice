import sys
input = sys.stdin.readline

n,m = map(int,input().split())

def two(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five(n):
    five = 0
    while n !=0:
        n = n // 5
        five += n
    return five

twos = two(n)-two(m)-two(n-m)
fives = five(n)-five(m)-five(n-m)

print(min(twos,fives))
