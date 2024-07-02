# [실습1] 글자를 입력 받습니다. input()->str
#       - 입력 받은 글자의(문자) 코드값을 출력합니다.

# msg=str(input())
# print(ord(msg))

# if msg==type(str):
#     print(ord(msg))

data=input("글자입력(a~z,A~Z): ")

if len(data)==1 and ('a'<=data<='z' or 'A'<=data<='Z'):
    print(f'{data}의 코드값: {ord(data)}')
else:
    print("1개의 알파벳 문자만 입력해야합니다.\n입력된 데이터를 확인하세요.")
# 문자==> 코드값 변환 내장함수: ord(문자1개)


# [실습2] 점수를 입력 받은 후 학점을 출력합니다.
# - 학점: A+,A,A-,B+,B,B-,C+,C,C-,D+,D,D-,F
# A+ : 96~100
# A: 95
# A-: 90~94
score=int(input('점수를 입력하세요.'))
grade=''

if score<0 or score>100:
    print(f'{score}는 잘못입력된 점수입니다.')
if score>95: grade='A+'
elif score==95: grade='A'
elif score>90: grade='A-'
elif score>85: grdae='B+'
elif score==85: grade='B'
elif score>80: grade='B-'
elif score>75: grdae='C+'
elif score==75: grade='C'
elif score>70: grade='C-'
elif score>65: grdae='D+'
elif score==65: grade='D'
elif score>60: grade='D-'
else: grade='F'
print(f'{score}는 {grade}학점입니다.')




# if 96<=score<=100:
#     print('A+')
# elif score == 95:
#     print('A')
# elif 90<=score<=94:
#     print('A-')
# elif 86<=score<=89:
#     print('B+')
# elif score == 85:
#     print('B')
# elif 80<=score<=84:
#     print('B-')
# elif 76<=score<=79:
#     print('C+')
# elif score == 75:
#     print('C')
# elif 90<=score<=74:
#     print('C-')
# elif 66<=score<=69:
#     print('D+')
# elif score == 65:
#     print('D')
# elif 60<=score<=64:
#     print('D-')
# else:
#     print('F')