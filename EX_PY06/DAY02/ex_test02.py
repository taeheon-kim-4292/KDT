#연산자 실습
# [실습1] 문자열 데이터 2개에 대한 논리 연산 수행 후 출력
data1="Hello"
data2='hello'

print(f'{data1} > {data2} and {data1} == {data2}: {data1>data2 and data1==data2}')
print(f'{data1} < {data2} or {data1} == {data2}: {data1>data2 or data1==data2}')






# [실습2] 정수 1개와 문자열 1개에 대한 논리 연산 수행 후 출력
#        단, not 연산자만 사용
# num=-3.2 , 0인 경우
# msg='원더우먼' , ''인 경우

num = -3.2
msg = '원더우먼'

print(f'not{num} : {not num}')
print(f'not{msg} : {not msg}')


# num = 0  #False
# msg='' #False

# print(f'not{num} : {not num}')
# print(f'not{msg} : {not msg}')