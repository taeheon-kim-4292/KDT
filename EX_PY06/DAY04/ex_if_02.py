# [실습2] 숫자를 입력 받아서 음이 아닌 정수와 음수 구분하기
# - 출력 : 숫자 -5는 음수입니다.
# number = int(input('아무 숫자나 입력하세요:'))

# if number <0:
#     print(f'숫자 {number}는 음수입니다.')
# elif number >0:
#     print(f'숫자 {number}는 양수입니다.')
# else:
#     print('0입니다.')

# [실습3] 점수를 입력 받아서 합격과 불합격을 출력
# - 합격: 60점이상

score=int(input('점수를 입력하세요:'))
if score >= 60:
    print('축하합니다. 합격입니다.')
else:
    print('불합격입니다.')

# [실습4] 점수를 입력 받아서 학점 출력
# - 학점: A,B,C,D,F

score=int(input('점수를 입력하세요:'))
if score >=90:
    print('당신은 A학점입니다.')
elif score <90 and score>=80:
    print('당신은 B학점입니다.')
elif score <80 and score>=70:
    print('당신은 C학점입니다.')
elif score <70 and score>=60:
    print('당신은 D학점입니다.')
else:
    print('당신은 F학점입니다.')