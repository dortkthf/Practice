n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    answer = 'yes'
    word_s = list(set(list(word)))
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i+1] not in word_s:
                answer = 'no'
                break
            else:
                word_s.remove(word[i])
        else:
            continue
    if answer != 'no':
        cnt+=1
print(cnt)