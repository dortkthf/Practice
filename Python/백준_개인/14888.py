# itertools 의 permutations를 사용하여 문제를 해결하기

from itertools import permutations

n = int(input())
nums = list(map(int,input().split()))

opers = list(map(int,input().split()))
opers2 = ['+','-','x','/']

operators = []

for i in range(len(opers)):
    for j in range(opers[i]):
        operators.append(opers2[i])

operlist = permutations(operators,len(operators))
operlist = set(operlist)

res = []

for i in operlist:
    for j in range(n):
        if j == 0:
            fst = nums[0]
            continue
        elif i[j-1] == '+':
            fst+=nums[j]
        elif i[j-1] == '-':
            fst-=nums[j]
        elif i[j-1] == 'x':
            fst*=nums[j]
        elif i[j-1] == '/':
            if fst<0:
                fst = -fst
                fst//=nums[j]
                fst = -fst
            else:
                fst//=nums[j]
    res.append(fst)

print(max(res),min(res),sep='\n')

