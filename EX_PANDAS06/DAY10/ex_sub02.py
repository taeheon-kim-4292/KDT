import csv
f= open(r'C:\Users\kdp\Desktop\KDT\EX_PANDAS06\subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)       # 한 줄을 읽고 다음 줄로 이동
print(header)


# ----분모가 0이라 에러가 발생
max_rate = 0
rate = 0
for row in data:
    for i in range(4,8):
        row[i] = int(row[i])    # 4,5,6,7 컬럼 값을 정수로 변환
    rate = row[4] / row[6]      # [6] 컬럼의 값이 0인 행 확인ㅇ ㅛㅇ도
    if rate > max_rate:
        max_rate = rate
print(max_rate)
f.close()
