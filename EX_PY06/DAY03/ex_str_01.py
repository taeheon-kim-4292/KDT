# -------------------------------------
# 문자열 str 데이터 다루기
# -------------------------------------
# 여러줄 문자열 ==> ''' ''' 또는 """ """ 
# msg="""
# 오늘은

# 좋은날
# 기쁜날
# # """

# print(f'msg=>{msg}')

#인덱싱: 문자열 안에 문자 한개 한개를 식별하는 방법
# - 원소/요소: 문자열 안에 문자 1개
# - 문법: 변수명[인덱스], 문자열데이터[인덱스]
# - 인덱스 종류
# * 왼쪽 >>> 오른쪽: 0,1, ...
# * 왼쪽 <<< 오른쪽: -2,-1, ...
# ------------------------------------------------
msg="Good"
msg2=''
#문자열 전체 출력
print(msg)

# 문자열 내 원소 출력
print(msg[0])
print(msg[-1])

# 원소/요소의 갯수를 파악해주는 내장함수 len()
# -원소/요소를 가지고 있는 데이터 타입에만 사용 가능
print(len(msg))

# 제일 마지막 원소/요소만 출력
print(msg[3], msg[len(msg)-1], msg[-1])

data="Happy New Year 2025! Good Luck"

print(f'인덱스 범위 : 0 ~ {len(data)-1}')
print(data[15:20])
print(data[15],data[16],data[17],data[18],data[19],sep='')  #인덱싱 및 슬라이싱 잘 알아두기 중요**

#슬라이싱: 문자열 내에 연속된 요소/원소 추출 방법
# - 문법: 변수명[시작:끝+1] 시작인덱스 이상 ~ 끝인덱스 미만

msg = "Life is too short, You need Python"
#Life만 출력하기
# 변수명[ :끝 인덱스]: 처음부터 의미
print(msg[0:4],msg[:4])
print(msg[0:3])
#You need Python만 출력하기
# 변수명[시작인덱스: ] : 끝까지 의미
print(msg[19:])
print(msg[:17])
# 변수명[:] : 처음부터 끝까지 의미
print(msg[:])


#슬라이싱: 문자열 내에 규칙/패턴을 가진 요소/원소 추출 방법
# - 문법: 변수명[시작:끝+1:간격] 
data='123456789'
#     012345678
# 2,4,6,8 만 추출하기
print(data[1], data[3], data[5], data[7])

# 인덱스가 2칸씩 증가하는 규칙
print(data[1:8:2])
print(data[1::2])

data='ABC1DEF2GHI3JKL4MNO5PQR6STU'
print(data[3::4])               #갯수 많으면 len(data)쓰면 편함