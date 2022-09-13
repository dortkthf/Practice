t = int(input())
for i in range(t):
    h,w,n = map(int,input().split())
    if n%h==0:
        print(100*h+(n//h))
    else:
        print((n%h*100)+(n//h)+1)