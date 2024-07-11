# - 매개변수의 전달되는 데이터가 지정되지 않는 경우
# - 어떤 데이터종류 = 데이터 ==> 키워드 파라미터/키워드 매개변수
# - 형식 def 함수명( **params) => 키=값
# 목적: 회원가입 기능 함수
# 함수이름: register
# 매개변수: 가입하는 사람마다 입력하는 정보가 모두 다름 **params
# 함수결과: 가입 메시지 str
def register(**params):
    print(type(params))

register(name='김태헌',job='의적')
register(id='master',age=10,gender='F')
register()

# 목적: 회원가입 기능 함수
# 함수이름: register2
# 매개변수: 필수 입력 사항 id,pw,email
#          선택 입력 사항 **params
# 함수결과: 가입 메시지 str
def register2(id,pw,email,**params):
    print(type(params))

register2("Hong","H12345","h@naver.com",gender='F')
register2("Hong","H12345","h@naver.com")
register2("Hong","H12345")