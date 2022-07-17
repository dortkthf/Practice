
for i in range(2,9+1) :
    print(f'{i}단')
    for j in range(1,9+1) :
        print(f'{i} X {j} = {i*j}')

def gugu(n):
    print(n, '단', sep='')
    for i in range(1, 9 + 1):
        print(f'{n} X {i} = {n * i}')

for i in range(2, 9 + 1):
    gugu(i)