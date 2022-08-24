import sys
input = sys.stdin.readline
sys.setrecursionlimit(500000)

# cnt = 0
cnt1 = 0

n = int(input())
# def fibo(n):
#     global cnt
#     if n == 1 or n == 2 :
#         cnt+=1
#         return 1
#     else:
#         cnt+=1
#         return fibo(n-1) + fibo(n-2)
# fibo(n)
d = [0]*(n+1)
d[1],d[2] = 1, 1
### Bottom_up 방식의 다이나믹 프로그래밍
### 다이나믹 프로그래밍이란 메모리 공간을 약간 더 사용해서 연산 속도를 비약적으로
### 증가시키는 방법이다.
### 다음과 같은 2가지 조건을 만족할 때 다이나믹 프로그래밍을 사용할 수 있다.
# 큰 문제를 작은 문제로 나눌 수 있다.
# 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]
    cnt1+=1

print(d[n])