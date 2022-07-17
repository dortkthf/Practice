mo = ['a', 'e', 'i', 'o', 'u']
word = input()
cnt = 0
for i in word :
    if i in mo :
        cnt += 1
print(cnt)