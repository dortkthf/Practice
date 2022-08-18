n = int(input())
extent = {

}
for _ in range(n):
    f_name,extension = input().split('.')
    if extension in extent:
        extent[extension] +=1
    else:
        extent[extension] = 1
ex1 = sorted(extent.items())
for ex in ex1:
    print(ex[0],ex[1])