n=int(input())
k = list(map(int,input().split()))

min = k[0]

for i in k :
    if min >= i :
        min = i
print(min)