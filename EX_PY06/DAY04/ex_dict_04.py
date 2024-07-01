# Dict 자료형 살펴보기
# - 연산자와 내장함수
person={'name': '홍길동','age':20, 'job':'학생'}
dog={'age': 5,'품종':'허스키','weight':'3kg','color':'검정','gender':'남'}
jumsu={'국어':90, '수학':178, '체육':100}
## [연산자]
# 산술 연산 X 
# 멤버 연산자: in, not in
#   key
print('name' in dog)
print('name' in person)

#   value : dict 타입에서는 key만 멤버 연산자로 확인
print('허스키' in dog)
print( 20 in person)

# value 추출
print('허스키' in dog.values())
print(20 in person.values())

# [내장함수]
# - 원소/요소 개수 확인: len()
print(f'dog의 요소 갯수: {len(dog)}개')
print(f'person의 요소 갯수: {len(person)}개')

## - 원소/요소 정렬: sorted()   
# - key만 정렬
print(f' jumsu 오름차순정렬 : {sorted(jumsu.values())}')   # 내림차순 reverse 안쓰면 오름차순 (default는 오름차순임)
print(f' jumsu 오름차순정렬 : {sorted(jumsu)}')  

print(f' jumsu 오름차순정렬 : {sorted(jumsu.items())}')
print(f' jumsu 오름차순정렬 : {sorted(jumsu.items(), key=lambda x:x[1])}')
# print(f'dog 오름차순정렬: {sorted(dog.values())}')
# TypeError: '<' not supported between instances of 'str' and 'int'

# 동일한 타입에서 정렬 가능함
