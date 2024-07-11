# 함수기반 계산기 프로그램
# -4칙연산 기능별 함수 생성 => 덧셈, 뺄셈, 곱셈, 나눗셈
# 2개 정수만 계산
# def cal(num1,num2):
#     if cal=='+': print(num1+num2)
#     elif cal=='-': print(num1-num2)
#     elif cal=='*': print(num1*num2)
#     elif cal=='/':print(num1/num2) if num2 !=0
def add(num1,num2):
    return num1+num2

def minus(num1,num2):
    return num1-num2

def gop(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2 if num2 else '0으로 나눌수 없음'

## 계산기 프로그램
## 사용자 종료를 원할때 종료 => 'x','X' 입력 시
#- 연산방식과 숫자 데이터 입력 받기
while True:
    # (1) 입력 받기
    req=input('연산(+,-,*,/)방식과 정수 2개 입력(예: + 10 2) : ')
    # (2) 종료 조건 검사
    if req == 'x' or req == 'X':
        print("계산기를 종료합니다.")
        break
    # (3) 입력에 연산방식과 데이터 추출 '+ 10 2'
    op,num1,num2 =req.split() # ['+','10','2]
    # str 정수==> int 변환
    num1=int(num1)
    num2=int(num2)
    # 연산방식에 따라서 계산 진행
    if op =='+': print(f'{num1}+{num2}={add(num1,num2)}')
    elif op =='-': print(f'{num1}-{num2}={minus(num1,num2)}')
    elif op =='*': print(f'{num1}*{num2}={gop(num1,num2)}')
    elif op =='/': print(f'{num1}/{num2}={div(num1,num2)}')   
    else:
        print(f'지원되지 않는 연산입니다.')