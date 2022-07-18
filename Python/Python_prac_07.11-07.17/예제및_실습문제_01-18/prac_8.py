numbers = list(map(int,input().split()))

if numbers[0] > numbers[1]:
    max = numbers[0]
    second = numbers[1]
else:
    max = numbers[1]
    second = numbers[0]

for i in numbers :
    if i>max :

        second = max
        max = i
    elif i>second :
        if i == max :
            continue
        second =i
print(second)