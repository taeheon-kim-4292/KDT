# 제어문 - while 반복문
# [실습] 사용자로부터 데이터를 입력 받습니다.
# 사용자 'q' 또는 'Q' 입력하기 전까지 입력을 받습니다.
# 'q'또는 'Q'를 입력하면 입력 받기를 중단하겠스빈다.
while True:
    data=input('데이터 입력(종료 q or Q) :')
    if data == 'q' or data =='Q':break

print("END")