
t = int(input())

for _ in range(t):
    n = int(input())
    
    fs = {}
    for i in range(n):
        name,kind = input().split()
        if kind in fs:
            fs[kind] += 1
        else:
            fs[kind] = 1
    mul = 1
    for i in fs:
        mul*=(fs[i]+1)
    print(mul-1)