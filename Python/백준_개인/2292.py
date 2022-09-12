1+0*6+1*6+2*6
n = int(input())
res=1
cnt=1
if n == 1:
    print(1)
else:
    for i in range(1,n):
        cnt+=1
        res+=(i*6)
        if res>=n:
            print(cnt)
            break