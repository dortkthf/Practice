h, m =map(int,input().split())
c = int(input())

if m+c>=60:
    h = h+((m+c)//60)
    m = (m+c)%60
    if h>=24:
        h = h-24
else:
    m+=c
print(h,m)