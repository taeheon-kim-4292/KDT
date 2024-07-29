import csv
f= open(r'C:\Users\kdp\Desktop\KDT\EX_PANDAS06\subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)       # 한 줄을 읽고 다음 줄로 이동
print(header)
max_rate =0
# ---------------------------
for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
    rate = row[4] / (row[4]+row[6])

    if row[6] == 0: # 무임승차 인원[6]이 없는 역 출력
        print(row)      # 디버깅 용도
f.close()
