t = int(input())
for i in range(t):
    h,w,n = map(int,input().split())
    if n%h==0:
        if n//h<10:
            print(f'{h}0{n//h}')
        else:
            print(f'{h}{n//h}')
    else:
        if n//h<10:
            print(f'{n%h}0{n//h+1}')
        else:
            print(f'{n%h}{n//h+1}')