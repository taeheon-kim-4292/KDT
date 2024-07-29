import csv
import matplotlib.pylab as plt
import koreanize_matplotlib

label = ['유임승차','유임하차','무임승차','무임하차']
color_list=['#ff9999','#ffc000','#8fd9b6','#d395d0']    # 파이 차트 컬러 값
pic_count = 0
with open(r'C:\Users\kdp\Desktop\KDT\EX_PANDAS06\subwayfee.csv', encoding='utf-8-sig') as f:
    data=csv.reader(f)
    next(data)


    for row in data:
        for i in range(4,8):
            row[i] = int(row[i])        # 정수형 변환
        print(row)
        plt.figure(dpi=100)     # 저장할 그림파일의 dpi 설정
        plt.title(row[3] + ' ' + row[1])
        plt.pie(row[4:8], labels=label, colors=color_list, autopct='%.1f%%', shadow=True)
        plt.savefig('img/' + row[3] + ' ' + row[1] + '.png')        # img 폴더 아래에 "지하철 이름 + 호선번호.png로 저장"
        plt.close()         # 파일닫기

        pic_count += 1
        if pic_count >= 10:
            break               # 10개 역의 파이차트만 저장