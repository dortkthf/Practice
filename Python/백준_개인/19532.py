a,b,c,d,e,f = map(int,input().split())

if c == 0 and f == 0:
    print(0,0)
elif a == 0:
    ansy = c//b
    ansx = (f-e*ansy)//d
    print(ansx,ansy)
else:
    ansy = (c*d-f*a)//(b*d-e*a)
    ansx = (c-b*ansy)//a

    print(ansx,ansy)