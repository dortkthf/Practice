# x값의 범위에 따른 y값을 계산 . 9%에서 오류뜸
# t = int(input())
# res = [[0, 0, 0] for i in range(101)]
# for _ in range(t):
#     x, y = map(int, input().split())
#     for i in range(x, x + 10):
#         if res[i][0] == 0:
#             res[i][0] = 1
#             res[i][1] = y
#             res[i][2] = y + 10
#         else:
#             if res[i][1] > y:
#                 res[i][1] = y
#             if res[i][2] < y + 10:
#                 res[i][2] = y + 10
# cnt = 0
# for i in range(101):
#     if res[i][0] != 0:
#         cnt += res[i][2] - res[i][1]
# print(cnt)

# 도화지를 전부 0인 100*100 리스트로 표현
n = int(input())
res = [list(0 for i in range(100)) for i in range(100)]
for i in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            res[i][j] = 1
cnt = 0
for i in res:
    cnt += sum(i)
print(cnt)
