# 조건부 표현식
# - 조건문을 1줄로 축약해주는 문법
# - 다중 조건문을 축약할 때 사용
# - 다른 프로그래밍 언어에서는 삼항연산자와 유사
# - 형식: 참실행코드 if 조건식 else 거짓실행코드

## [실습1] 임의의 숫자 데이터를 정하기
##         해당 숫자 데이터가 짝수인지 홀수인지 판별하는 코드

# num=int(input())

num=7

# 비교연산으로 조건 판별
if num%2 ==0:
    print("짝수")
else:
    print("홀수")

# 값으로 조건 판별
if num%2:
    print("홀수")
else:
    print("짝수")

# not 연산자로 조건 판별
if not num%2:
    print("짝수")
else:
    print("홀수")

## ==> 1줄로 조건식 축약: 조건부 표현식
print("짝수") if num%2 ==0 else print("홀수")
print("홀수") if num%2 else print("짝수")
print("짝수") if not num%2 else print("홀수")