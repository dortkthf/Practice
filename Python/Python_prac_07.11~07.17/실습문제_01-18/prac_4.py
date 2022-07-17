n = int(input())
cnt=1
mul=1
while cnt<=n :

    mul*=cnt
    cnt+=1
print(mul)

n=int(input())
cnt=1
mul=1
for i in range(n):
    mul*=cnt
    cnt+=1
print(mul)