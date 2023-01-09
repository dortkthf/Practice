n,m = map(int, input().split())
nm = list(input() for i in range(n))

nn = n-8
mm = m-8
dp = []
res = []

for i in range(nn+1):
    for j in range(mm+1):
        dp.append([i,j])

for d in dp:
    base = 'W'
    cnt = 0
    for i in range(d[0],d[0]+8,2):
        for j in range(d[1],d[1]+8,2):
            if nm[i][j] != base :
                cnt+=1
            if nm[i+1][j] == base :
                cnt+=1
        for j in range(d[1]+1,d[1]+8,2):
            if nm[i][j] == base: 
                cnt+=1
            if nm[i+1][j] != base:
                cnt+=1
    res.append(cnt)

    base = 'B'
    cnt = 0
    for i in range(d[0],d[0]+8,2):
        for j in range(d[1],d[1]+8,2):
            if nm[i][j] != base :
                cnt+=1
            if nm[i+1][j] == base :
                cnt+=1
        for j in range(d[1]+1,d[1]+8,2):
            if nm[i][j] == base: 
                cnt+=1
            if nm[i+1][j] != base:
                cnt+=1
    res.append(cnt)

print(min(res))
