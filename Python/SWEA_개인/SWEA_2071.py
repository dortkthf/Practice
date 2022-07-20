n = int(input())

for i in range(1,n+1):
    numbers = list(map(int,input().split()))
    result = round(sum(numbers)/len(numbers))
    print(f'#{i} {result}')