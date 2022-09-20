n = int(input())
res=[]
if n>=5:
    five=n//5
    for i in range(five+1):
        cnt=i
        num=n-i*5
        if num%3==0:
            cnt+=num//3
            res.append(cnt)
        else:
            continue
else:
    if n%3==0:
        res.append(n//3)
if res:
    print(min(res))
else:
    print(-1)