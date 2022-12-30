# import sys
# input = sys.stdin.readline

## 교훈 재귀를 통해서 return 값을 받을때에 import sys를 사용하면 안받아진다.
cnt = 0

def recursion(s, l, r):
    global cnt
    cnt+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

t = int(input())
for _ in range(t):
    word = input()
    print(isPalindrome(word),cnt)
    cnt=0