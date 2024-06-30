# 내장함수 range()
# - 숫자 범위를 생성하는 내장함수
# - 형식 : range(시작숫자, 끝숫자+1, 간격)
#          range(끝숫자+1) : 0~끝숫자
# [실습1] 1~100 숫자를 저장하세요
nums=range(1,101)
print(f'nums 값 : {nums}\n타입 : {type(nums)}\n개수 : {len(nums)}')

# 원소/요소 읽기===> 인덱싱
print(nums[0], nums[-1])

# 원소/요소 여러개 읽기 ===> 슬라이싱
print(nums[0:10], nums[30:41])
# 원소/요소 하나하나를 보기 ==> list/tuple 형변환
print(list(nums[0:10]), tuple(nums[30:41]))

# [실습1] 1~100에서 3의 배수만 저장하세요.
# => 3,6,9,12 ... 99
three=range(3,101,3)
print(list(three))

# [실습1] 1.0 ~ 10.0 사이에 숫자 저장
data=list(range(1,11))
print(data)
# float(data[0]) ==> map() 내장함수 사용
# map ==> list 형변환
data=list(map(float,data))
print(data)
