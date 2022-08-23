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
