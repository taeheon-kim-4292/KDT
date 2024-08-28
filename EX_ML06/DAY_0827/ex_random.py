# 임의의 숫자 즉, 난수 추출 
# - random 모듈 존재
# - 0.0 ~ 1.0 사이 실수 추출 
# - n ~ m 정수 추출
# - random 값 고정 ==> seed 기능 
# import random
# for _ in range(10):
#     print(random.random())


# # 얘는 고정된 값만 나옴
# random.seed(10)
# for i in range(10):
#     print(random.random())

X = [[10],[3],[9],[5],[7],[12],[67],[91],[45],[2],[17]]
y =[1,2,3,4,5,6,7,8,9,10,11]
from sklearn.model_selection import train_test_split

# 섞어서 학습용/테스트용 데이터셋 분리 
# random에서 seed 설정 역할 매개변수 => random_state
X_train, X_test,y_train,y_test = train_test_split(X,y,random_state=10)
print(f'X : {X}')
print(f'X_train : {X_train}')
print(f'X_test : {X_test}')


# 섞어서 학습용/테스트용 데이터셋 분리 
# random에서 seed 설정 역할 매개변수 => random_state
X_train, X_test,y_train,y_test = train_test_split(X,y)
print(f'X : {X}')
print(f'X_train : {X_train}')
print(f'X_test : {X_test}')