def rectangle(a, b):
    area = a*b
    circum = (a+b)*2
    return area, circum
a, b = map(int,input().split())
print(rectangle(a, b))
