# 제어문 - 반복문 중단 break
# - 반복을 중단 시키는 조건문과 함께 사용 됨
# [실습] 숫자 데이터의 합계가 30이상이 되면 더 이상 합계를 하지 마세요
# 숫자 데이터는 1~50으로 구성되어있습니다.
# nums=list(range(1,51))
# total=0
# for n in nums:
#     if total>=30:
#         break
#     total=total+n
# print(f'total=>{total}{1}~{n-1}까지의 합계')

# [실습] 4개 과목점수가 있다
# 과목 점수가 1과목이라도 40이하면 불합격임
# 4개과목 평균이 60이상이어야 함

jumsu=[89,39,80,77]
isPass=True                 # Flag 변수
for n in jumsu:
    if n< 40: 
        print('불합격')
        isPass=False
        break
    print('모든 과목이 40점 이상입니다.')
# # 합/불 처리   
if isPass:
    agv=sum(jumsu)/len(jumsu)
    if agv>=60:
        print(f'당신은 {agv}점으로 합격입니다')
    else:
        print(f'당신은 {agv}점으로 불합격입니다.')
else:
    print(f'당신은 40미만인 과목으로 불합격입니다.')