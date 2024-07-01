<<<<<<< HEAD
# Dict 자료형 살펴보기
# - 데이터의 의미를 함께 저장하는 자료형
# - 형태: {키:값(데이터), 키2:값, ...키n:값}
# - 키는 중복 X , 값은 중복 O
# - 데이터 분석 시 파일 데이터 가져올 때 자주 사용

## [Dict 생성]
data={}
print(f'data => {len(data)}개, {type(data)}, {data}')

# 사람에 대한 정보: 이름,나이,성별
data={'name':'마징가','age':100, 'gender':'남'}
print(f'data => {len(data)}개, {type(data)}, {data}')

# 강아지에 대한 정보: 품종, 무게, 색상, 성별, 나이
dog={'age': 5,'품종':'허스키','weight':'3kg','color':'검정','gender':'남'}
print(f'data => {len(dog)}개, {type(dog)}, {dog}')

## [Dict 원소/요소 읽기]
## - 키를 가지고 값/데이터 읽기
## - 형식: 변수명[키]
dog={'age': 5,'품종':'허스키','weight':'3kg','color':'검정','gender':'남'}

# 색상 출력
print(f'색상:{dog["color"]}')
print(f'품종:{dog["품종"]}, 성별:{dog["gender"]}')

## [Dict 원소/요소 변경]
# - 변수명[키] = 새로운 값
# 나이 5살 ==> 6살
dog["age"] = 6
print(dog)

# 몸무게 3kg ==> 8kg
dog["weight"]='8kg'
print(dog)

## - del 변수명[키] 또는 del(변수명[키])
## 성별 데이터를 삭제
del dog["gender"]
print(dog)

## 추가: 변수명[새로운 키] = 값
## 이름 추가
dog["name"]="마루"
=======
# Dict 자료형 살펴보기
# - 데이터의 의미를 함께 저장하는 자료형
# - 형태: {키:값(데이터), 키2:값, ...키n:값}
# - 키는 중복 X , 값은 중복 O
# - 데이터 분석 시 파일 데이터 가져올 때 자주 사용

## [Dict 생성]
data={}
print(f'data => {len(data)}개, {type(data)}, {data}')

# 사람에 대한 정보: 이름,나이,성별
data={'name':'마징가','age':100, 'gender':'남'}
print(f'data => {len(data)}개, {type(data)}, {data}')

# 강아지에 대한 정보: 품종, 무게, 색상, 성별, 나이
dog={'age': 5,'품종':'허스키','weight':'3kg','color':'검정','gender':'남'}
print(f'data => {len(dog)}개, {type(dog)}, {dog}')

## [Dict 원소/요소 읽기]
## - 키를 가지고 값/데이터 읽기
## - 형식: 변수명[키]
dog={'age': 5,'품종':'허스키','weight':'3kg','color':'검정','gender':'남'}

# 색상 출력
print(f'색상:{dog["color"]}')
print(f'품종:{dog["품종"]}, 성별:{dog["gender"]}')

## [Dict 원소/요소 변경]
# - 변수명[키] = 새로운 값
# 나이 5살 ==> 6살
dog["age"] = 6
print(dog)

# 몸무게 3kg ==> 8kg
dog["weight"]='8kg'
print(dog)

## - del 변수명[키] 또는 del(변수명[키])
## 성별 데이터를 삭제
del dog["gender"]
print(dog)

## 추가: 변수명[새로운 키] = 값
## 이름 추가
dog["name"]="마루"
>>>>>>> 6b4b6469270e48dca5d2bee00bb2a7a3ede2875e
print(dog)