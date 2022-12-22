n = int(input())
# if n == 1:
#     pass
# else:
while n != 1:
    for i in range(2, n + 1):
        if n % i == 0:
            print(i)
            n = n // i
            break
    if n == 1:
        break
