n = int(input())

for i in range(1,n+1):
    numbers = list(map(int,input().split()))
    max = numbers[0]
    for number in numbers:
        if max < number:
            max = number
    print(f'#{i} {max}')