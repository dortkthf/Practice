w, h, b= map(int,input().split())
result = (w*h*b/8/1024/1024)
final = format(result,'.2f')
print(final,'MB')