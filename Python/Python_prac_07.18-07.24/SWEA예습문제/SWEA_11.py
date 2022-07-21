n = int(input())

for i in range(1,n+1):
    t1,m1,t2,m2 = map(int,input().split())
    time = t1+t2
    minute = m1+m2
    if time>12 :
        time-=12
    if minute>60:
        minute-=60
        time+=1
    print(f'#{i} {time} {minute}')