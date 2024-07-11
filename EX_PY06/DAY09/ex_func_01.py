# 함수(Function)이해 및 활용
# 함수이름: 3개의 정수를 덧셈한 후 결과를 반환하는 함수
# 함수기능: add3
# 매개변수: num1, num2, num3
# 함수결과: 정수 result
def add3(num1,num2,num3):
    result=num1+num2+num3
    return result

# 함수이름: 3개의 정수를 곱셈한 후 결과를 반환하는 함수
# 함수기능: multi3
# 매개변수: num1, num2, num3
# 함수결과: 정수 result
def multi3(num1,num2,num3):
    result=num1*num2*num3
    return result

# 함수이름: 2개의 정수를 나눗셈한 후 결과를 반환하는 함수
# 함수기능: div
# 매개변수: num1, num2
# 함수결과: None

# # 내 꺼
def div(num1,num2):
    print(num1/num2) if num2 != 0 else None

## result 사용 차이?? 위에껄로 써도되는지??

def div(num1,num2):
    if not num2:        # not 0 ==> True        # 정수에서 0은 FALSE
        result='0으로 나눌 수 없음'
    else:
        result=num1/num2
    print(f'{num1}/{num2}={result}')

## 함수 사용하기 즉, 호출----------------------
## 덧셈하기
vaule=add3(1,2,3)

## 나눗셈하기
value1=div(3,4)
print(value1)

