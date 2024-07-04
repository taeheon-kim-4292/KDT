# List/Set/Dict 자료형과 반복문, 조건부 표현식 결합
# - 메모리 사용량 감소 & 속도 빠름

# [실습] A 리스트의 데이터를 B 리스트에 담기
#   단, A 리스트에서 짝수값은 3을 곱하고 홀수값은 그대로 담기
a=[1,2,3,4,5,6]
b=[]
for n in a:
    if n%2:
        b.append(n)
    else:
        b.append(n*3)
print(f'a=>{a}\nb=>{b}')
# [1] 모든 원소를 새로운 리스트에 담기
# c=[n for n in a]
# print(f'a=>{a}\nb=>{b}\nc=>{c}')

# [2] 짝수 데이터만 새로운 리스트 C에 담기
# for n in a:
#     if not n%2: c.append(n*3)
c=[n*3 for n in a if not n%2]
print(f'a=>{a}\nb=>{b}\nc=>{c}')

# [3] 짝수 데이터는 3을 곱하고 홀수 데이터는 그대로 새로운 리스트 C에 담기
# for n in a:
#     if not n%2: c.append(n*3)
#     else: c.append(n)
c=[n*3 if not n%2 else n for n in a]
print(f'a=>{a}\nb=>{b}\nc=>{c}')