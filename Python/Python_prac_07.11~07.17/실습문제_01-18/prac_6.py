from re import I


numbers = list(map(int,input().split()))
max = numbers[0]
for i in numbers :
    if max >= i :
        max = max
    else :
        max = i
print(max)