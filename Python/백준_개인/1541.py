mini = input()
mini_len = len(mini)

str = ''

res = []
ans = 0
for i in range(mini_len):
    if mini[i].isdigit():
        str+=mini[i]
        if i == mini_len-1:
            res.append(str)
    elif mini[i] == '+':
        res.append(str)
        str=''
    elif mini[i] == '-' :
        res.append(str)
        str=''
        res.append(mini[i])

minus = False

for i in res:
    if i.isdigit() and minus == False:
        ans+=int(i)
    elif i == '-':
        minus = True
    elif i.isdigit() and minus == True:
        ans-=int(i)
print(ans)