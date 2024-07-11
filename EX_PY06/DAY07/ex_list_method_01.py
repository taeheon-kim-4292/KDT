# list 전용의 함수 즉, 메서드(Method)
# - list 원소/요소를 제어하기 위한 함수들
import random as rad
#[1]실습 데이터=> 임의의 정수 숫자 10개 구성된 리스트
for num in range(10):
    print(rad.randint(1,10))

datas=[7,3,9,11,3,7,3,1,8,4]

# Method - 요소 인덱스를 반환하는 메서드 index()
# -> 11의 인덱스 찾기
# -> 왼쪽>>>오른쪽으로 찾기
idx=datas.index(11)
print(f'11의 인덱스: {idx}')

# -> 0의 인덱스를 찾기  ==> 존재하지 않는 데이터의 경우 ERROR
if 0 in datas:
    idx=datas.index(0)
    print(f'0의 인덱스: {idx}')
else:
    print("0은 존재하지 않는 데이터입니다.")

# -> 3의 인덱스 찾기    졸앗
# if 3 in datas:
#     idx= datas.index(3)
#     idx =datas.index(3,2)
#     print(f'첫번째3의 인덱스: {idx}')

#     idx=datas.idx(3,idx+1)

# 메서드 - 데이터가 몇개 존재하는지 갯수 파악하는 메서드 method count(데이터)
cnt=datas.count
print(f' 3의 개수 ; {cnt}')

for i in range(cnt):
    idx=datas.index(3,idx if not i else idx+1)