
word = input()
leng = len(word)
for i in range(leng) :
    before = ord(word[i])
    after = chr(before-32)
    print(after, end = '')
