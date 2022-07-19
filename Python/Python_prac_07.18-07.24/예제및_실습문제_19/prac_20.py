n=int(input())
n=str(n)
sum1=0

for i in n :
    sum1+=int(i)
print(sum1)

n=input()
list = list(map(int,n))
result=sum(list)
print(result)

result=0
number = int(input())
while number:
    result+=number%10
    number//=10
print(result)