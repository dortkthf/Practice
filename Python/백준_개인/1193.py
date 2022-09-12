n = int(input())
res = 0
for i in range(2*n):
    res+=i
    if res>=n:
        num = n-sum(range(i))
        if i%2==0:
            print(f'{1+(num-1)}/{i-(num-1)}')
            break
        else:
            print(f'{i-(num-1)}/{1+(num-1)}')
            break