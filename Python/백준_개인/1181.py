import sys
input = sys.stdin.readline

n = int(input())
ls = set()
for _ in range(n):
    word = input().rstrip()
    ls.add((len(word), word))
ls = list(ls)
ls.sort()
for cnt, word in ls:
    print(word)

# 교훈 중복을 없앨때 for문 안에서 if 문으로 하게되면 시간이 많이 소모된다
# 반면에 중복을 for 문이 끝나고 나서 set함수로 없애고 정렬을 다시하면 시간이 더빨라진다
