# 모듈: 변수, 함수, 클래스가 들어있는 파이썬 파일
# 패키지: 동일한 목적의 모듈들을 모은 것
#        여러개의 모듈 파일들이 존재
# 모듈 사용법: import 모듈파일명    <---확장자 제외
import random as ran

# # 임의의 숫자를 생성해서 추출하기
# # 임의의 숫자 10개 생성
# # => random()   : 0.0 <= ~ < 1.0
for cnt in range(10):
    print( int(ran.random()*10))        # 0이상 1미만

# -> randint(a,b)       : a<= ~ <=b
for cnt in range(10):
    print(ran.randint(0,1))

## [실습] 로또 프로그램을 만들어주세요
## 1 ~ 45 범위에서 중복되지 않는 6개를 추출하세요
## 반복의 횟수는 알수없음       => 알수없음
## 무한 반복문
## 종료 조건 = 중복되지 않은 6개 숫자  => list, set, dict

# list 사용
lotto=[0,0,0,0,0,0]
idx=0
while True:
    num = ran.randint(1,45)
    if num not in lotto:
        lotto[idx] = num
        idx=idx+1
    if idx==6: break
print(lotto)


# # dict 사용
lotto={}
key=1
while len(lotto)<=6:
    num = ran.randint(1,45)
    if num not in lotto.values():
        lotto[key] = num
        key=key+1
print(lotto)

# set 사용
lotto=set()
key=1
while len(lotto)<6:
    num = ran.randint(1,45)
    num_set=set([num])
    lotto=lotto.union(num_set)
print(lotto)

# ----------------------------
# set 타입의 add() 메서드:  원소 추가, 중복 시 추가X
lotto=set()
while len(lotto)<6:
    num = ran.randint(1,45)
    lotto.add(num)
print(lotto)

