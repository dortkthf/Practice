n = int(input())
result = []
for i in range(1,n+1):
    if n%i == 0:
        result.append(i)
for i in result:
    print(i, end = ' ')