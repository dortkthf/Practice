from sys import stdin
input = stdin.readline

n = int(input())
ls = []
for _ in range(n):
    x,y = map(int,input().split())
    ls.append([y,x])
ls.sort()
for x,y in ls:
    print(y,x)

# 교훈 리스트를 key=lambda:x x[1] 로 정렬을 하게되면
# x[1]을 기준으로 정렬을 하게 되지만 x[0] 의 정렬은 마음대로 되게된다