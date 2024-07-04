# 매서드 - 요소 순서 제어 메서드 reverse()
import random as rad
rad.seed(3) # 동일한 랜덤 숫자 추출을 위한 기준점
datas=[]
for _ in range(10):
    datas.append(rad.randint(1,30))

print(f'{len(datas)}개, {datas}')

## 0번 -> -1번으로 , -1번을 0번으로
datas.reverse()
print(f'{len(datas)}개, {datas}')

# 메서드 - 요소 크기를 비교해서 정렬해주는 메서드 sort()
# - 기본 정렬: 오름차순 즉, 작은 데이터부터 큰 데이터 순서로 정렬
datas.sort()
print(f'{len(datas)}개, {datas}')

# 내림차순 큰 거부터 작은거
datas.sort(reverse=True)
print(f'{len(datas)}개, {datas}')

# 메서드 - 리스트에서 요소를 꺼내는 메서드 pop()
# - 꺼내면 리스트에서 삭제됨
# - 제일 마지막 놈이 튀어나옴
value=datas.pop()
print(f'value: {value} - {len(datas)}개, {datas}')

value=datas.pop(0)      # 특정 인덱스의 원소/요소 꺼내기
print(f'value: {value} - {len(datas)}개, {datas}')

# 메서드 - 리스트 확장 시켜주는 메서드 extend()
datas.extend([11,22,33])
print(f'value: {value} - {len(datas)}개, {datas}')

datas.extend((555,777))
print(f'value: {value} - {len(datas)}개, {datas}')

datas.extend('Good Luck')
print(f'value: {value} - {len(datas)}개, {datas}')

datas.extend({555,777,555,777})
print(f'value: {value} - {len(datas)}개, {datas}')

datas.extend({'name': '홍길동', 'age':12})
print(f'value: {value} - {len(datas)}개, {datas}')

# 메서드 - 모든 원소 삭제 메서드 clear()
datas.clear()
print(f'{len(datas)}개, {datas}')








