import sys
input = sys.stdin.readline

n,k = map(int,input().split())
tmp = 0
for i in range(1,n+1):
    if n%i == 0:
        tmp+=1
        if tmp == k:
            print(i)
            break
else:
    if tmp < k:
        print(0)