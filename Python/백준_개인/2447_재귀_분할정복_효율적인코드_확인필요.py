n = int(input())
star = [list('*' for i in range(n)) for i in range(n)]
cnt = 0
def stars(n):
    global cnt
    if n>3 :
        cnt+=1
        stars(n//3)
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

# n = int(input())

# llist = []
# def star(l):
#     if l == 3:
#         return ['***','* *','***']

#     arr = star(l//3)
#     llist.append(l)
#     stars = []

#     for i in arr:
#         stars.append(i*3)

#     for i in arr:
#         stars.append(i+' '*len(arr)+i)

#     for i in arr:
#         stars.append(i*3)

#     return stars
# for i in star(n):
#     print(*i)
# print(llist)

n = int(input())
stars = ['***','* *','***']
def makestars(n) :
    if n == 3:
        return stars
    starss = makestars(n//3)
    l = []
    for s in starss:
        l.append(s*3)
    for s in starss:
        l.append(s+' '*len(starss)+s)
    for s in starss:
        l.append(s*3)
    return l

for i in makestars(n):
    print(*i,sep='')