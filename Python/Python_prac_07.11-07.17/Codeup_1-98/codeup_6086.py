n = int(input())
sum = 0
cnt = 0
while True :
    sum+=cnt
    cnt+=1
    if sum >= n :
        print(sum)
        break
n = int(input())
sum = 0
for i in range(n) :
    sum+=i
    if sum >= n :
        print(sum)
        break