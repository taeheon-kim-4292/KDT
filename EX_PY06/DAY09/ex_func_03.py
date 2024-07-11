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

#- 함수기능: 계산기 메뉴를 출력하는 함수
#- 함수이름: print_menu
#- 매개변수: X
#- 함수결과: X  함수 결과가 없어도 () 넣어야함
def print_menu():
    print(f'{"*":*^16}')
    print(f'{"계 산 기":^16}')
    print(f'{"*":*^16}')
    print(f'{"*  1 덧  셈  *":16}')
    print(f'{"*  2 뺄  셈  *":16}')
    print(f'{"*  3 곱  셈  *":16}')
    print(f'{"*  4 나눗셈  *":16}')
    print(f'{"*  5 종  료  *":16}')
    print(f'{"*":*^16}')

# print(f'{"계산기":*^16}')         #가운데 정렬
# print(f'{"*":*>16}')         #오른쪽 정렬
# print(f'{"*":*<16}')         #왼쪽 정렬

#- 함수기능: 연산 수행 후 결과를 반환하는 함수
#- 함수이름: calc
#- 매개변수: 함수명, str 숫자 2개, str연산자 기호
#- 함수결과: X
def calc(func,num1,num2,op):
    num1=int(num1)
    num2=int(num2)
    print(f'결과: {num1}{op}{num2}{func(num1,num2)}')









## 계산기 프로그램
#- 사용자에게 원하는 계산을 선택하는 메뉴 출력
#- 종료 메뉴 선택 시 프로그램 종료
# => 반복 ----> 무한반복: While 사용
while True:
    # 메뉴 출력
    print_menu()

    # 메뉴 선택 요청
    choice = input('메뉴 선택:')
    if choice.isdecimal():
        choice=int(choice)
    else:
        print("0~9사이 숫자만 입력하세요")  
        continue     
    # 종료 조건 처리(5번 메뉴 선택)
    if choice == 5:
        print("프로그램을 종료합니다.")
        break
    elif choice ==1:    # 덧셈
        print("덧셈")
        num1,num2 = input("정수 2개(예: 10 2 )").split()
        calc(add,num1,num2,'+')
        print(f'==> 결과: {num1}+{num2}={add(num1,num2)}')
    elif choice ==2:    # 뺄셈
        print("뻴셈")
        num1,num2 = input("정수 2개(예: 10 2 )").split()
        calc(minus,num1,num2,'-')
        print(f'==> 결과: {num1}-{num2}={minus(num1,num2)}')
    elif choice ==3:    # 곱셈
        print("곱셈")
        num1,num2 = input("정수 2개(예: 10 2 )").split()
        calc(gop,num1,num2,'*')
        print(f'==> 결과: {num1}*{num2}={gop(num1,num2)}')
    elif choice ==4:    # 나눗셈
        calc(div,num1,num2,'/')
        print(f'==> 결과: {num1}/{num2}={div(num1,num2)}')
    else:
        print("잘못선택했습니다")