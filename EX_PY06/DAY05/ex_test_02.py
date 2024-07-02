## [실습] 임의의 숫자가 5의 배수 여부 결과를 출력하세요
## 단 5를 제외한 나머지는 고려하지 않습니다
# num=int(input())
# print('5의 배수입니다.') if num % 5 ==0 else print('5의 배수가 아닙니다')

## [실습] 문자열을 입력 받아서 문자열의 원소 개수를 저장
## - 단 원소 개수가 0이면 None 저장
## (1) 입력받기 input()
## (2) 원소/요소 개수 파악 len()
## (3) 원소/요소 개수 저장 단, 0인경우 None 저장하기

# data=input()

# # print(len(data)) if len(data)>0 else print(None)


# if len(data):
#     result=len(data)
# else:
#     result=None

# result=len(data) if len(data) else None
# print(f'{data}의 원소/요소 개수: {result}개')

## [실습] 연산자(4칙연산자 + - * /)와 숫자 2개 입력 받기
## - 입력된 연산자에 따라 계산 결과 저장
## - 예) 입력: + 10 3 출력:13

# n1 = input()
# n2 = int(input())
# n3 = int(input())


# if n1 == '+':
#     print(n2+n3)
# elif n1 == '-':
#     print(n2-n3)
# elif n1 == '*':
#     print(n2*n3)
# else:
#     print(n2/n3)

command = input("4칙연산자 1개와 숫자 2개 입력\n(예: + 10 3): ").split()
#split()은 공백 기준으로 문자를 나누는것 
print(command)

if command[0]=='+': 
    result= int(command[1]+int(command[2]))
elif command[0]=='-':
    result= int(command[1]-int(command[2]))
elif command[0]=='*':
    result= int(command[1]*int(command[2]))
elif command[0]=='/':
    result= int(command[1]/int(command[2]))
else:
    print("4칙연산자가 아닙니다.")
