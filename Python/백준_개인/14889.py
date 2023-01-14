from itertools import combinations

n = int(input())
nums = list(range(n))

s = list(list(map(int,input().split())) for i in range(n))

nlist = list(combinations(list(range(n)),n//2))

res = []

for i in range(len(nlist)//2):
    nums2 = set(nums)
    a = nlist[i]
    b = nums2-set(nlist[i])
    b = list(b)
    a_scores = 0
    b_scores = 0
    for j  in list(combinations(a,2)):
        a_scores+=s[j[0]][j[1]]+s[j[1]][j[0]]
    for j in list(combinations(b,2)):
        b_scores+=s[j[0]][j[1]]+s[j[1]][j[0]]
    res.append(max(a_scores,b_scores)-min(a_scores,b_scores))
print(min(res))