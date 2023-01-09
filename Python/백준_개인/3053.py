# 소수점 자릿수 표현에는 format 을 사용하여 표현할수 있다 이외에도 f-string 도있다.

import math

r = int(input())
ans = round(math.pi*(r**2),6)
ans2 = round((r**2)*2,6)
print(format(ans, '.6f'))
print(format(ans2, '.6f'))