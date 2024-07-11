# 사용자 정의 함수
# 2개 정수 덧셈 함수 요청
def addTwo(num1,num2): pass

# 5개 정수 덧셈 함수 요청
def addFive(num1,num2,num3,num4,num5):pass

# 3개 정수 덧셈 함수 요청
def addThree(num1,num2,num3): pass

# 목적: 매개변수의 개수를 유동적으로
#       0개 ~ n개 까지 가능하도록
# 형태: def 함수명( *변수명) <= 0개 ~ N개 데이터

# 정수를 덧셈 한 후 결과를 반환하는 함수
# 매개 변수: 0개 ~ N개
# 함수 결과: 덧셈 계싼 값 result
def add(*nums):
    total=0
    for n in nums:
        total+=n
    return total
# 함수 호출
print(add())
print(add(1,1,1))
print(add(8,9,11,22,55,11,6,7))












