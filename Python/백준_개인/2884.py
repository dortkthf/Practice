h, m = map(int,input().split())
if h==0 and m<45:
    new_h = ((24*60+m)-45)//60
    new_m = ((24*60+m)-45)%60
else:
    new_h = ((60*h+m)-45)//60
    new_m = ((60*h+m)-45)%60

print(new_h, new_m)