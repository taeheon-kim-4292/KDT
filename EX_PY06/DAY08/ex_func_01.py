# 사용자 정의 함수
# 함수 기능: 2개의 정수를 덧셈 한 후 결과를 반환/리턴하는 함수
# 함수 이름: add
# 매개 변수: 2개, num1, num2
# 함수 결과: 덧셈 계산 값 result
def add(num1,num2):
    result=num1+num2
    return result

# 함수 사용하기 즉, 함수 호출
# 함수명(data)
value =add(10,20)

# 함수의 매개변수 개수와 다른 데이터 전달 X ERROR
# value=(10,20,30,)     # 많아서 에러
# value=add(10)         # 부족해서 에러
print(value)