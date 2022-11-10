n = int(input())
numbers = list(map(int, input().split()))
d = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1
print(max(d))
