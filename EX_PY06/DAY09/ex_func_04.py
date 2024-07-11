
# 함수기능: 3개의 정수를 곱셈한 후 결과를 반환하는 함수
# 함수이름: multi
# 매개변수: num1, num2, num3
# 함수결과: 정수(result) 반환

def add(num1,num2):
    return num1+num2


def multi(num1, num2):
    result= num1*num2
    return result



# 함수기능: 2개의 정수를 나눈 후 결과를 출력하는 함수
# 함수이름: div
# 매개변수: num1, num2
# 함수결과: 실수(result) 반환

def div(num1,num2):
    if not num2:
        result= ('0으로 나눌 수 없습니다.')
    else: result= (num1/num2)
    return result

def minus(num1,num2):
    result= num1-num2
    return result

#연산수행 후 결과를 반환하는 함수
# 이름: cal
# 매개변수: 함수명, str숫자2개
# 함수결과:none(바로 출력)

def cal(func, op):
    data=input('정수 2개(예:10 2):')
    if check_data(data,2):
        data=data.split()
        print(f'결과: {data[0]} {op} {data[1]} = {func(int(data[0]),int(data[1]))}')
    else:
        print("올바른 데이터가 아닙니다")

#- 함수기능: 입력 받은 데이터가 유효한 데이터인지 검사하는 함수
#- 함수이름: check_data
#- 매개변수: str 데이터(ex:10 3), 데이터 개수
#- 함수결과: True False

# def check_data():
#     if len(num1,num2) >2:
#         result=False
#     elif len(num1,num2)<=2:
#         result=True
# print(check_data)
def check_data(data,count):
    # 입력된 str 데이터 ==> list로 형변환: split()
    data=data.split()
    # 갯수 체크
    if len(data)==count:
        # 0~9로 구성된 str인지 체크
        isOk=True
        for d in data:
            if not d.isdecimal():
                isOk=False
                break
        return isOk
    else:
        return False
        





# 함수기능: 계산기 메뉴를 출력
# 함수이름: print_menu
# 매개변수: 없음
# 함수결과: 없음

def print_menu():
    print(f'{"*":*^16}')
    print(f'{"   계  산  기":16}')
    print(f'{"*":*^16}')
    print(f'{"*  1 덧    셈  *":16}')
    print(f'{"*":*^16}')
    print(f'{"*  2 뺄    셈  *":16}')
    print(f'{"*":*^16}')
    print(f'{"*  3 곱    셈  *":16}')
    print(f'{"*":*^16}')
    print(f'{"*  4 나 눗 셈  *":16}')
    print(f'{"*":*^16}')
    print(f'{"*  5 종    료  *":16}')
    print(f'{"*":*^16}')
# 계산기 프로그램
# 사용자가 원하는 계산을 선택하는 메뉴 출력
# 종료 메뉴 선택시 프로그램 종료

# 사용자가 번호를 선택해서 연산할 수 있도록
# 예시 1. 덧셈 2. 뺄셈 .... 5. 종료
# 종료 전까지 반복
while True:
    print_menu()

    choice= (input("메뉴 선택:"))
    if choice.isdecimal():
        choice=int(choice) 
    else:
        print('0~5사이 숫자만 입력하세요')
        continue
    if choice ==5:
        print("프로그램을 종료합니다.")
        break
    elif choice ==1: 
        print("덧셈")
        num1, num2= input('정수 2개를 입력하세요').split()
        cal(add, num1, num2, '+')
    elif choice ==2: 
        print("뺄셈")
        num1, num2= input('정수 2개를 입력하세요').split()
        cal(minus, num1, num2, '-')
    elif choice ==3: 
        print("곱셈")
        num1, num2= input('정수 2개를 입력하세요').split()
        cal(multi, num1, num2, '*')
    elif choice ==4: 
        print("나눗셈")
        num1, num2= input('정수 2개를 입력하세요').split()
        cal(div, num1, num2, '/')
    else: print('선택된 메뉴가 없습니다')        


