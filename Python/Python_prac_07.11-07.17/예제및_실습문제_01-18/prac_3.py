n = int(input())
cnt=1
sum=0
while cnt<=n:
    
    sum+=cnt
    cnt+=1
print(sum)

n2 = int(input())
cnt=0
sum=0

for i in range(n):
    cnt+=1
    sum+=cnt
print(sum)