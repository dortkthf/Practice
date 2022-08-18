t = int(input())
for i in range(1,t+1):
    word = input()
    for chr in word:
        if chr in 'aeiou':
            word=word.replace(chr,'')
    print(f'#{i} {word}')