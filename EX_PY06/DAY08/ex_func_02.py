# 사용자 정의 함수
# 함수 기능: 2개의 정수를 덧셈 한 후 결과를 반환/리턴하는 함수
# 함수 이름: add
# 매개 변수: 2개, num1, num2
# 함수 결과: 없음
# 리턴 값 필요없으면 그냥 안적으면된다
# def add(num1,num2):
#     result=num1+num2
#     print(f'{num1}+{num2}={result}')

# # 함수 사용하기 즉, 호출
# add(5,8)

# # 사용자 정의 함수
# # 함수 기능: 인사 메시지를 출력하는 함수
# # 함수 이름: hello
# # 매개 변수: 없음
# # 함수 결과: 없음
# def hello():
#     print("Hello~^^")

# 함수기능: 원하는 단의 구구단을 출력해주는 기능 함수
# 함수 이름: gop
# 매개 변수: num
# 함수 결과:
def gop(num):
    for n in range(1,10):
        print(f'{num}*{n}={num*n}')

gop(7)


# 함수 기능: 파일의 확장자를 반환해주는 기능 함수
# 함수 이름: hwak
# 매개 변수:
# 함수 결과:
# def hwak(file):
#     for f in file:
#         dot=file.find('.')
#     print(file[dot+1:])

# hwak('tftlol.txt','fafaef.xlx','dfdddf.hwp')


def hwak(file):
    print(file[file.rfind('.')+1:])
    
hwak('tftlol.txt')

