def solution(my_string, overwrite_string, s):
    answer = ''
    for i in range(s):
        answer+=my_string[i]
    else:
        answer+=overwrite_string
    for i in range(s+len(overwrite_string),len(my_string)):
        answer+=my_string[i]
    return answer