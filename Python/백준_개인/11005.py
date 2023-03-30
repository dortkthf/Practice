import sys
input = sys.stdin.readline

n,b = list(map(int,input().split()))

ans = []
cnt = 0

while True:
    if n < b**cnt:
        cnt-=1
        break
    cnt+=1

for i in range(cnt,-1,-1):
    a = n//(b**i)
    n-=a*(b**i)
    if a >= 10:
        ans.append(chr(a+55))
    else:
        ans.append(a)

print(*ans,sep='')