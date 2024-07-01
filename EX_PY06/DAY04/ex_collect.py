# Collection 자료형의 공통적인 부분 살펴보기
## [여러개의 변수에 데이터 저장]
# name='홍길동'
# age=12
# job='의적'
# gender='남'

# 팩킹(packing) 방식  :  변수명 = tuple 타입    ==> 인덱싱 접근
data='홍길동',12,'의적','남'

# 언팩킹 방식: 변수1, 변수2, ...변수n = tuple 타입
#             변수명 갯수 == 데이터 수
name,age,job,gender='홍길동',12,'의적','남'
print(name,age,job,gender)

# name, age = '홍길동',12, '의적','남'  => ERROR
name, age, _, _, ='마징가',100,'의적','남'
print(name,age,_)


jumsu=[100,99]
kor,math = [100,99]
print(jumsu,kor,math)

person={'name':'박', 'age':11}
k1,k2={'name':'박','age':11}
print(person,k1,k2)

# 생성자(constructor) 함수: 타입명과 동일한 이름의 함수
# - int(), float(), str(), list(), tuple(), dict(), set()
# -map(), range()
# 기본 데이터 타입
num = int(10)           #num=10
fnum= float(10.2)       #fnum=10.2
msg=str('Good')         #msg='Good'
isOK=bool(False)        #isOK=False
print(num,fnum,msg,isOK)

# 컬렉션 데이터 타입
lnums = list([1,2,3,4])   # nums=[1,2,3,4]
tnums = tuple((3,6,9))    # tnums=(3,6,9)
ds = dict(d1=10, d2=30)   # ds={'d1':10, 'd2':30}
ss = set({1,1,3,3,5})     # ss={1,1,3,3,5}
print(lnums,tnums,ds)

# 타입 변경 = 형변환
# dict 자료형은 다른 자료형과 달리 데이터 형태가 다름
# - 데이터 형태=> key:값
# - dict(키1=값, 키2=값, . . .) : 키는 str만 가능, ''나 "" 사용불가 ****************************
# 딕셔너리 키에는 홀따옴표 X

ds = dict(name=1, age=2, gender='남')
print(ds)

ds = dict([('name','마징가'), ('age',12)])
print(ds)

# 내장함수: zip()=> 같은 인덱스의 요소끼리 묶어줌
l1=['name','age','gender']
l2=['마징가',12,'남']
l3=[False,True,True]
print(list(zip(l1,l2,l3)))

ds=dict(zip(l1,l2))
print(ds)