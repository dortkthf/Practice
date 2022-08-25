import sys
input = sys.stdin.readline
sys.setrecursionlimit(500000)

cnt1 = 0
cnt = 0

n = int(input())
def fibo(n):
    global cnt
    if n == 1 or n == 2 :
        cnt+=1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
fibo(n)

d = [0]*(n+1)
d[1],d[2] = 1, 1
for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]
    cnt1+=1

print(d[n])