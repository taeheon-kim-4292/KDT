# [실습] 10번 숫자 데이터를 입력을 받습니다.
# - 숫자 데이터를 모두 더해서 합계가 30이상이 되면
# 10번 입력 안 받았더라도 종료해주세요.
total=0
for cnt in range(10):
    data=int(input('숫자 입력: '))
    total=total+data
    if total >=30: break

    
















# data=int(input('원하는 숫자 입력: ')).split()
# total=0
# isBreak=False
# for n in data:
#     total=total+n
#     if total >= 30:
#         isBreak=True
#         break
#     if isBreak:
#         break
