T = int(input())
for i in range(1,T+1):
    a,b = map(int,input().split())
    mok = a//b
    na = a%b
    print(f'#{i} {mok} {na}')