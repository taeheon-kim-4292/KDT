# 제어문 - 반복문

# - 유사하거나 동일한 코드를 1번 작성으로 재사용하기 위한 방법
# - 종류: for, while 

## for 반복문 
## - 시퀀스(이터러블) 데이터에서 원소/요소를 하나씩 읽어올 때 사용
## - 형식
## - for 변수명 in 시퀀스/이터러블 데이터: 
##   ----반복실행 될 코드

#[실습] 문자열에서 문자를 1줄에 1개씩 출력하기
# msg="Merry Christmas 2025"
# # m=msg[0],msg[1]...
# # m말고 아무거나 넣어도 되는건가??
# for m in msg: 
#     print(m,ord(m),end='')
    
# [실습] 리스트에서 원소를 하나씩 읽어오기
# 1~100 범위에서 3의 배수만 저장한 리스트
# data=list(range(3,101,3))

# for d in data:
#     print(d,end=' ')

# [실습] str 타입의 원소를 가지는 리스트입니다.
# 해당 원소를 정수로 형변환 시켜서 저장해주세요
# 원래 원소의 값을 변경해야 하는 경우는 인덱스 필요
# - 원소 개수 ===> 인덱스 범위
data=['4','9','1','3','8']

for a in data:
    a=int(a)

# 리스트의 인덱스
for idx in range(len(data)):
    print(f'idx=>{idx}')
    data[idx]=int(data[idx])

