# [실습] 메세지를 입력받습니다.
# 알파벳 대문자인 경우 소문자로, 소문자인 경우 대문자로
# 나머지는 그대로 출력합니다.

# msg="Hello World!"
# for m in msg:
#     if 'A' <= m <='Z':
#         print(m.lower(),end='')
#     elif 'a' <= m <='z':
#         print(m.upper(),end='')
# else:
#     print(m,end='')

# 문자 ==> 코드: ord(문자1개)
# 코드 ==> 문자: chr(정수코드값)
# ch='A'

# # 대문자를 소문자로 바꾸는것
# print(chr(ord('A')+32))

# # 소문자를 대문자로 바꾸는것
# print(chr(ord('a')-32))

#
msg=input('메시지를 남겨주세요: ')

for m in msg:
    if 'A'<=m<='Z':
        print(chr(ord(m)+32),end='')
    elif 'a'<=m<='z':
        print(chr(ord(m)-32),end='')
    else:
        print(m,end='')

