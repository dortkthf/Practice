import sys
sys.stdin = open('SWEA_2063_input.txt','r')

n =int(input())
numbers = list(map(int,input().split()))
numbers.sort()
middle = int((n-1)/2)
print(numbers[middle])

