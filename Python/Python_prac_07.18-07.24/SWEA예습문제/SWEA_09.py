n= int(input())

for i in range(1,n+1):
    complete = [0,1,2,3,4,5,6,7,8,9]
    result=[]
    num = int(input())
    for j in range(1,10**4):
        mulnum = num*j
        strnum=str(mulnum)
        for snum in strnum :
            if int(snum) not in result:
                result.append(int(snum))
        if sorted(result) == complete:
            print(f'#{i} {strnum}')
            break




