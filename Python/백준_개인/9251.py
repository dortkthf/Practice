a = input()
b = input()

alen = len(a)
blen = len(b)
if alen>blen:
    big = a
    small = b
else:
    big = b
    small = a

dp = []
for i in range(len(big)):
    for j in range(len(small)):
        if small[j] == big[i] and j not in dp:
            dp.append(j)

res = [1 for i in range(len(dp))]

for i in range(1,len(dp)):
    for j in range(i):
        if dp[i]>dp[j]:
            res[i] = max(res[j]+1,res[i])

print(max(res))