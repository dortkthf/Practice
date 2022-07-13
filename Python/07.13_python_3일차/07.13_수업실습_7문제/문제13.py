word = input()
empty = ''
for i in range(len(word)-1,-1,-1) :
    empty+=word[i]
print(empty)