### 답은 나오지만 시간초과

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
cnt = 1
a = 0
while True:
    if a == 0:
        newa = 1
    tmp = newa
    newa += a
    a = tmp
    cnt+=1
    if cnt == n:
        break
print(newa)


## 이것도 답은 나오지만 시간초과

n = int(input())

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
print(fibonacci(n))



# 정답 잘나옴
a = 0
b = 1
n = int(input())
for i in range(1,n):
    a,b = b, a+b
print(b)

# 다이나믹 프로그래밍 탑 다운을 통한 문제 해결

n = int(input())
d = [0]*(n+1)

def fibo(n):

    if n == 0 or n == 1:
        d[n] = n
        return d[n]
    elif d[n] == 0:
        d[n] = fibo(n-1)+fibo(n-2)
        return d[n]
    else:
        return d[n]
print(fibo(n))