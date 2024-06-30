# 입력 & 출력 실습
# [실습1] 데이터 저장 및 변수 생성 및 출력
# - 생년월일 
# - 띠
# - 혈액형
# - 출력형태: 나는 0000년 00월 00일 000띠입니다
# - 혈액형은 __________인 OO형 입니다.
birth = "1999년 10월 25일"
ani = "토끼띠"
blo = "A형"

print(f"나는 {birth} {ani}입니다.")
print(f"혈액형은 소심한{blo}입니다.")

# [실습2] 입력 받은 데이터 저장 (단, 파일로 저장)
# - 좋아하는 계절
# - 좋아하는 나라
# - 여행가고 싶은 나라

FILENAME= 'infor.txt'
f=open(FILENAME,'w',encoding='utf-8')       #한글 깨지면 encoding='utf-8'
print(f"좋아하는 계절은 겨울이고 좋아하는 나라는 일본이며 여행가고 싶은 나라도 일본입니다.",file=f)
f.close()

#강사님 답안
season = input("좋아하는 계절:")
country = input("좋아하는 나라:")
country1 = input("여행가고 싶은 나라:")

FILENAME1 = 'info2.txt'
f=open(FILENAME1, mode='w' , encoding='utf-8')
f.write(season)
f.write('\n')       #줄바꿈 문자
f.write(country)
f.write('\n')
f.write(country1)
f.close()

#답안2
print(f'좋아하는 계절   :{season}',file=f)
print(f'좋아하는 나라   :{country}',file=f)
print(f'여행 가고 싶은 나라   :{country1}',file=f, end='')

f.close()