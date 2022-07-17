from pickletools import int4


numbers = list(map(int,input().split()))
min = numbers[0]
for i in numbers :
    if min <= i :
        min = min
    else :
        min = i
print(min)