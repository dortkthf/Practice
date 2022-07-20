n = int(input())
for i in range(1,n+1):
    numbers = list(map(int,input().split()))
    result=0
    for number in numbers:
        if number % 2 == 1:
            result+=number
    print(f'#{i} {result}')