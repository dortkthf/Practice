n = int(input())
result=[1]
for i in range(1,n+1):
    result.append(2**i)
for i in result:
    print(i,end=' ')