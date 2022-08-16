word = input()
for i in 'abcdefghijklmnopqrstuvwxyz':
    if i in word:
        print(word.index(i),end=' ')
    else:
        print(-1,end=' ')