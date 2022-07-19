
n= int(input())
reverse =[]
revnum = 0
for i in range(n):
    reverse.append(n%10)
    n//=10
    if n==0:
        break

for i in range(len(reverse)):
    revnum+=reverse[i]*(10**(len(reverse)-1-i))
print(revnum)

n = int(input())
result=0
while n>0 :
    na = n%10
    result=result*10+na
    n=n//10
print(result)


n=int(input())
result=0
for i in range(n):
    last = n%10
    result=result*10+last
    n//=10
    if n==0 :
        break
print(result)

n=int(input())
result=0
while n:
    result = 10*result
    result+= n%10
    n//=10
print(result)