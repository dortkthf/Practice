# n= int(input())

# for i in range(1,n+1):
#     complete = [0,1,2,3,4,5,6,7,8,9]
#     result=[]
#     num = int(input())
#     for j in range(1,10**4):
#         mulnum = num*j
#         strnum=str(mulnum)
#         for snum in strnum :
#             if int(snum) not in result:
#                 result.append(int(snum))
#         if sorted(result) == complete:
#             print(f'#{i} {strnum}')
#             break

# n = int(input())

# for i in range(1,n+1):
#     complete=[0,1,2,3,4,5,6,7,8,9]
#     result = []
#     number = int(input())
#     cnt=0
#     while True:
#         cnt+=1
#         nummul=number*cnt
#         strnummul=str(nummul)
#         for snum in strnummul:
#             if int(snum) not in result:
#                 result.append(int(snum))
#         if complete==sorted(result):
#             print(f'#{i} {nummul}')
#             break



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    N1 = N
    numbers = set()
    while True:
        for n in str(N):
            numbers.add(n)
        if len(numbers) == 10:
            break
        N += N1
    print(f'#{test_case} {N}')