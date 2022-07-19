t = int(input())
for i in range(1,t+1):
    numbers = list(map(int,input().split()))
    sum = 0
    for num in numbers :
        sum+=num
    aver = round(sum/len(numbers))
    print(f'#{i} {aver}')
