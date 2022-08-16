n = int(input())

for i in range(1,n+1):
    number = input()
    year,month,day = '','',''
    for j in range(4):
        year=year+number[j]
    for k in range(4,6):
        month=month+number[k]
    for l in range(6,8):
        day=day+number[l]
    if int(month) <= 12 :
        if int(month) in [1,3,5,7,8,10,12]:
            if int(day)>=1 and int(day)<=31:
                print(f'#{i} {year}/{month}/{day}')
            else:
                print(f'#{i} -1')
        elif int(month) in [4,6,9,11]:
            if int(day)>=1 and int(day)<=30:
                print(f'#{i} {year}/{month}/{day}')
            else:
                print(f'#{i} -1')
        elif int(month) == 2:
            if int(day)>=1 and int(day)<=28:
                print(f'#{i} {year}/{month}/{day}')
            else:
                print(f'#{i} -1')
        else :
            print(f'#{i} -1')

