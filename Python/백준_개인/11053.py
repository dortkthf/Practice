n = int(input())
numbers = list(map(int,input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    cnt=0
    for j in range(i):
        print(numbers[j])
    print(cnt)
    cnt+=1