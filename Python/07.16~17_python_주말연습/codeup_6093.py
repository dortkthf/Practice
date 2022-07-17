n = int(input())
num = list(map(int,input().split()))
num = num[::-1]
for i in range(n):
    print(num[i], end = ' ')