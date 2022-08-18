t = int(input())
for _ in range(t):
    n, numbers, numdic = int(input()),list(map(int,input().split())),{}
    for num in numbers:
        if num in numdic:
            numdic[num]+=1
        else:
            numdic[num]=1
    mxvalues = max(numdic.values())
    result = []
    for k, v in numdic.items():
        if v == mxvalues:
            result.append(k)
    result.sort(reverse=True)
    print(f'#{n} {result[0]}')
