n = int(input())
for i in range(1,n+1):
    N = int(input())
    sum=0
    for j in range(1,N+1):
        if j % 2 == 0:
            sum-=j
        else :
            sum+=j
    print(f'#{i} {sum}')