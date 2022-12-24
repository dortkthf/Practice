res = []
for i in range(1,10001):
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        res.append(i)
T = int(input())

for _ in range(T):
    n = int(input())
    a = n//2
    for i in range(5000):
        if i<n and a-i in res and a+i in res:
            print(a-i,a+i)
            break