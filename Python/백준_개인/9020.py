res = []
for i in range(2,10001):
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        res.append(i)

T = int(input())
for _ in range(T):
    n = int(input())
    cnt = []
    r = []
    for i in res:
        if i>n/2:
            break
        for j in res:
            if i+j == n and i<=j:
                r.append([i,j])
                cnt.append(j-i)
                break
    a = cnt.index(min(cnt))
    print(*r[a])