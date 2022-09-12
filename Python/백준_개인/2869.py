a,b,v = map(int,input().split())

if a==v:
    print(1)
elif (v-a)/(a-b)<1:
    print(2)
else:
    if (v-a)%(a-b)==0:
        print(1+((v-a)//(a-b)))
    else:
        print(2+((v-a)//(a-b)))
