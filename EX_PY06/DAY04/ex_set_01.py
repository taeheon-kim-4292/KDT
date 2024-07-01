# Set 자료형 살펴보기
# - 여러가지 종류의 여러 개 데이터를 저장
# - 단, 중복 불가!
# - 컬렉션 타입의 데이터 저장 시 Tuple가능
# - 형태 : {데이터1, 데이터2,... 데이터n}

## [Set 생성] 
data=set()
print(f'data의 타입: {type(data)}, 원소/요소 갯수: {len(data)}개, 데이터 : {data}')

# 여러개 데이터 저장한 set
data={10,30,20,-9,10,30,10,30,10,10}
print(f'data의 타입: {type(data)}, 원소/요소 갯수: {len(data)}개, 데이터 : {data}')

data={9.34,'Apple',10,True,'10'}
print(f'data의 타입: {type(data)}, 원소/요소 갯수: {len(data)}개, 데이터 : {data}')


# data={1,2,3,[1,2,3]}
# print(f'data의 타입: {type(data)}, 원소/요소 갯수: {len(data)}개, 데이터 : {data}')
# TypeError: unhashable type: 'list'

data={1,2,3,(1,2,3)}
print(f'data의 타입: {type(data)}, 원소/요소 갯수: {len(data)}개, 데이터 : {data}')

data={1,2,3,(1)}            # 쉼표 안찍는 이상 튜플이 되는게 아닌 정수라서 중복됨
print(f'data의 타입: {type(data)}, 원소/요소 갯수: {len(data)}개, 데이터 : {data}')

data={1,2,3,(1,)[0]}
data={1,2,3,{1:100}}        # 변경할 수 없는 tuple만 가능 dic X
print(f'data의 타입: {type(data)}, 원소/요소 갯수: {len(data)}개, 데이터 : {data}')

#set() 내장함수
# 다양한 타입 ==> set 변환
data=set([1,2,1,2,3]) # ===> set([1,2,3])
data=set("Good")   # emptySet
print(data)

data=list("GOod")
print(data)

# Set 자료형 살펴보기
# - 여러가지 종류의 여러 개 데이터를 저장
# - 단, 중복 불가!
# - 컬렉션 타입의 데이터 저장 시 Tuple가능
# - 형태 : {데이터1, 데이터2,... 데이터n}

## [Set 생성] 
data=set()
print(f'data의 타입: {type(data)}, 원소/요소 갯수: {len(data)}개, 데이터 : {data}')

# 여러개 데이터 저장한 set
data={10,30,20,-9,10,30,10,30,10,10}
print(f'data의 타입: {type(data)}, 원소/요소 갯수: {len(data)}개, 데이터 : {data}')

data={9.34,'Apple',10,True,'10'}
print(f'data의 타입: {type(data)}, 원소/요소 갯수: {len(data)}개, 데이터 : {data}')


# data={1,2,3,[1,2,3]}
# print(f'data의 타입: {type(data)}, 원소/요소 갯수: {len(data)}개, 데이터 : {data}')
# TypeError: unhashable type: 'list'

data={1,2,3,(1,2,3)}
print(f'data의 타입: {type(data)}, 원소/요소 갯수: {len(data)}개, 데이터 : {data}')

data={1,2,3,(1)}            # 쉼표 안찍는 이상 튜플이 되는게 아닌 정수라서 중복됨
print(f'data의 타입: {type(data)}, 원소/요소 갯수: {len(data)}개, 데이터 : {data}')

data={1,2,3,(1,)[0]}
data={1,2,3,{1:100}}        # 변경할 수 없는 tuple만 가능 dic X
print(f'data의 타입: {type(data)}, 원소/요소 갯수: {len(data)}개, 데이터 : {data}')

#set() 내장함수
# 다양한 타입 ==> set 변환
data=set([1,2,1,2,3]) # ===> set([1,2,3])
data=set("Good")   # emptySet
print(data)

data=list("GOod")
print(data)

