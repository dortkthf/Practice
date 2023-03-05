import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    tmp = 0
    ans = []
    for i in range(1,n):
        if n%i == 0:
            tmp+=i
            ans.append(i)
    if tmp == n:
        print(n,end=' = ')
        print(*ans,sep=' + ')
    else:
        print(n,'is NOT perfect.')