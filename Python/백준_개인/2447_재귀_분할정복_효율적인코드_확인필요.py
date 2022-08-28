n = int(input())
star = [list('*' for i in range(n)) for i in range(n)]
cnt = 0
def stars(n):
    global cnt
    if n>3 :
        n/=3
        cnt+=1
        stars(n)
        n*=3
        cnt-=1
    a = int(n/3)   
    for x in range(3**cnt):
        for y in range(3**cnt):
            for i in range(a,int(2*a)):
                for j in range(a,int(2*a)):
                    star[int(i+n*x)][int(j+n*y)] = ' '
    return star
stars(n)
for s in star:
    print(*s,sep='')
