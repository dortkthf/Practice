# while 문 해결

n = int(input())
count = 0
result = 0
while count<=n :
    result+=count
    count+=1
print(result)

# for문 해결

n = int(input())

result = 0
count = 1
for i in range(n) :
    result+=count
    count+=1
print(result)