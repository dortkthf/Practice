word = input()
res = {}

for i in word :
    if i in res :
        res[i]+=1
    else :
        res[i] = 1

for a, b in res.items() :
    print(a, b)
