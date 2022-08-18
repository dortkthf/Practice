# number = input()
# cnt = 0
# if int(number)//10 == 0:
#     if int(number)%3==0:
#         print(cnt)
#         print('YES')
#     else:
#         print(cnt)
#         print('NO')
# else:        
#     numy = sum(list(map(int,number)))
#     cnt = 1
#     if numy//10 == 0:
#         if numy%3==0:
#             print(cnt)
#             print('YES')
#         else:
#             print(cnt)
#             print('NO')
#     else:
#         while True:
#             numy = sum(list(map(int,str(numy))))
#             cnt+=1
#             if numy//10 == 0:
#                 if numy%3==0:
#                     print(cnt)
#                     print('YES')
#                     break
#                 else:
#                     print(cnt)
#                     print('NO')
#                     break

n = input()
cnt = 0

def easy(n,cnt):
    if len(n) == 1:
        if int(n)%3 == 0:
            print(cnt)
            print('YES')
        else:
            print(cnt)
            print('NO')
    else:
        new= str(sum(list(map(int,n))))
        cnt+=1
        easy(new,cnt)

easy(n,cnt)
