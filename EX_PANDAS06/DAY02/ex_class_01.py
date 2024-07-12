# 클래스 (Class)
# - 객체지향언어(00P)에서 데이터를 정의하는 자료형
# - 데이터를 정의할 수 있는 데이터가 가진 속성과 기능 명시
# - 구성요소 : 속성/attribue/field + 기능/method
# 클래스 정의: 햄버거를 나타내는 클래스
# 클래스 이름: burger
# 클래스 속성: 번, 패티, 야채, 치즈
# 클래스 기능: 햄버거 설명 기능

class Burger:
    
    kind="맥도날드"
    # 힙 영역에 객체 생성 시 속성값 저장 기능
    def __init__(self,bread,patty,veg):
        self.bread=bread
        self.patty=patty
        self.veg=veg
        # self.kind=kind

    # 클래스의 기능 즉 메서드
    def printInfo(self):
        print(f'브랜드 : {self.kind}')        
        print(f'빵 종류 : {self.bread}')
        print(f'패티 종류 : {self.patty}')
        print(f'야채 종류 : {self.veg}') 

## 객체 생성
# 불고기 버거 객체생성
Burger1=Burger('브리오슈','불고기','양상추 양파 토마토')
# 치즈 버거 객체생성
Burger2=Burger('참깨방','쇠고기패티','치즈')              

# 버거 정보 확인
Burger1.printInfo()
Burger2.printInfo()