# [3] 논리연산자 
# - 종류: and, or, not
# - 특징: 여러개의 경우에 대한 결과를 바탕으로 결론 도출
# - and: 결과1 and 결과2 and 결과3 
#        결과1,2,3 모두 True인 경우만 True가 됨

num1=8
num2=3

print(f'{num1}>0 and {num2}>0 : {num1>0 and num2>0}')
print(f'{num1}>0 and {num2}==0 : {num1>0 and num2==0}')


# - or: 결과1 or 결과2 or 결과3 
#        결과1,2,3 중 1개 이상 True가 되면 True 결론

print(f'{num1}>0 or {num2}>0 : {num1>0 or num2>0}')
print(f'{num1}>0 or {num2}==0 : {num1>0 or num2==0}')
print(f'{num1}==0 or {num2}==0: {num1==0 or num2==0}')

# - not: not 결과
#        결과에 반대로 결론을 도출
#       True ==> False, False ==>True로 결론

print(f'not{num1}>0 : {not num1>0}')
