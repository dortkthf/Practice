# 1
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    b = list(range(1,n+1))
    newb = []
    for i in range(k):
        for j in range(1,n+1):
            newb.append(sum(b[:j]))
        b = newb
        newb = []
    print(b[n-1])

# 2
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    b = list(range(1,n+1))

    for i in range(k):
        for j in range(1,n):
            b[j]+=b[j-1]
    print(b[-1])