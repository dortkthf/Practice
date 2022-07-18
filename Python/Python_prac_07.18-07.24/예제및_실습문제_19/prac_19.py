#방법 1

number = 123
number = f'{number}'
print(number, type(number))
cnt=0
for i in number:
    cnt+=1
print(cnt)

# 방법 2
number = int(input())
cnt=0
for i in range(number):
    cnt+=1
    number=number/10
    if number<10 :
        cnt+=1
        break
print(cnt)