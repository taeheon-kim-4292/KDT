# [실습] 모든 구구단을 출력하세요

for dan in range(1,10):
    print(f'{dan}단')
    for n in range(1,10):
        print(f'{dan}*{n} = {dan*n}')


## dan 2~9
for n in range(2,10):
    print(n)
    #1~9 숫자
    for m in range(1,10):
        print(f'{n}*{m}={n*m}')