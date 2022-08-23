n = int(input())
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))

while True:
    n = input('\n팩토리얼 구할 숫자는?? ')
    if n.isnumeric():
        res = factorial(int(n))
        print(res)
    else:
        print('종료합니다.')
        break