n = int(input())
nums = [int(input()) for i in range(n)]

cnt = 0
nn = 1

stacks = []
res = []

for i in range(1,(2*n)):
    if nn > n:
        nn = n
    elif len(res) == 2*n:
        break
    elif len(stacks) !=0 and stacks[-1] == nums[cnt]:
        stacks.pop()
        res+=['-']
        cnt+=1
    elif nn != nums[cnt]:
        stacks+=[nn]
        res+=['+']
        nn+=1
    elif nn == nums[cnt]:
        res+=['+','-']

        cnt+=1
        nn+=1

if len(stacks) == 0:
    print(*res,sep='\n')
else:
    print('NO')