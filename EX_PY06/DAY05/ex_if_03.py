# ==> 조건부 표현식: 조건이 2개 이상인 경우
## [실습1] 숫자가 양수, 0, 음수 인지 판별
num=9
if num>0:
    print('양수')
elif num<0:
    print('음수')
else:
    print(0)

result='양수' if num>0 else '음수' if num<0 else print(0)
result='양수' if num>0 else()

