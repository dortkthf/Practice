word = input()
word2 = ''
for i in range(len(word)) :
    if word[i] != 'a':
        word2+=word[i]
print(word2)