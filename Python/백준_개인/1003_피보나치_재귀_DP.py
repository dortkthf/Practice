# bottom up 방식을 이용한 DP로 풀기

t = int(input())
for _ in range(t):
    n = int(input())
    cnt1 = [0, 1]
    cnt0 = [1, 0]
    def fibo(n):
        if n >= len(cnt1):
            for i in range(len(cnt1),n+1):
                cnt1.append(cnt1[i-1]+cnt1[i-2])
                cnt0.append(cnt0[i-1]+cnt0[i-2])
    fibo(n)
    print(cnt0[n],cnt1[n],sep=' ')

# 일반 재귀함수로 풀기 시간초과 걸림

t = int(input())
for _ in range(t):
    n = int(input())
    cnt1 = 0
    cnt0 = 0
    def fibo(n):
        global cnt1, cnt0
        if n == 1:
            cnt1+=1
            return 5
        elif n == 0:
            cnt0+=1
            return 5
        else:
            return fibo(n-1)+fibo(n-2)
    fibo(n)
    print(cnt0,cnt1,sep=' ')