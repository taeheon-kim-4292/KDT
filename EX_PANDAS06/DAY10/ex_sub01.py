import csv
f= open(r'C:\Users\kdp\Desktop\KDT\EX_PANDAS06\subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)       # 한 줄을 읽고 다음 줄로 이동
print(header)
max_rate =0
i=1
for row in data:
    print(row)
    if i > 5:
        break
    i += 1
f.close()