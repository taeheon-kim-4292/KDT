# [실습] 출력하고 싶은 단을 입력 받아서
#       해당 단의 구구단을 출력하세요

#[출력 예시] 2 * 1 = 2
dan=int(input())
nums=[1,2,3,4,5,6,7,8,9]
# for n in nums:
#     print(f'{dan} * {n} = {dan*n}')

for n in range(1,11):
    print(f'{dan}*{n} = {dan*n}')

