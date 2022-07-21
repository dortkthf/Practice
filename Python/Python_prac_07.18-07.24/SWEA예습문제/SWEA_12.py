n = int(input())

for i in range(1,n+1):
    ilist = list(str(i))
    clap =''
    for ilnum in ilist:
        if int(ilnum) in [3,6,9]:
            clap+='-'
            i = clap
        else :
            i = i
    print(i,end=' ')