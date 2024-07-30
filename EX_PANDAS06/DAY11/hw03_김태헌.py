import	csv
import	matplotlib.pyplot as	plt
import	platform
import	math
import	koreanize_matplotlib

    
def calculate_population():
    f = open(r'C:\Users\kdp\Desktop\KDT\EX_PANDAS06\data\gender.csv',encoding='euc_kr')
    data=csv.reader(f)
    city_list=['대구광역시', '대구광역시 중구', '대구광역시 동구', '대구광역시 서구', 
            '대구광역시 남구', '대구광역시 북구', '대구광역시 수성구', 
          '대구광역시 달서구', '대구광역시 달성군', '대구광역시 군위군']
    sum_male_list = []
    sum_female_list = []
    for city in city_list:       
        for row in data:
            male_list=[]
            female_list=[]
            if city in row[0]:
                for i in range(106,207):
                    male_num = int(row[i].replace(',',''))
                    female_num = int(row[i+103].replace(',',''))
                    male_list.append(male_num)
                    female_list.append(female_num)
                break    
        
        print(f'{city}: (남:{sum(male_list)} 여:{sum(female_list)})')
        sum_male_list.append(sum(male_list))
        sum_female_list.append(sum(female_list))
    f.close()
    # f, axes = plt.subplots(5, 2)
    # #그래프 사이 간격 추가
    # f.subplots_adjust(hspace=0.5,wspace=0.3)
    # def draw_pie_chart(ax, male, female, city):
    #     ax.pie([male, female], labels=['남성', '여성'], autopct='%1.1f%%', startangle=90)
    #     ax.set_title(city)
    # draw_pie_chart(axes[0][0], sum_male_list[0], sum_female_list[0], city_list[0])
    plt.figure(figsize=(12, 8))

    # plt.subplot(5, 2, 1)
    # plt.pie([sum_male_list[0], sum_female_list[0]], labels=['남성', '여성'], autopct='%1.1f%%', startangle=90)
    # plt.title(city_list[0])

    # plt.subplot(5, 2, 2)
    # plt.pie([sum_male_list[1], sum_female_list[1]], labels=['남성', '여성'], autopct='%1.1f%%', startangle=90)
    # plt.title(city_list[1])

    for i in range(10):
        plt.subplot(5, 2, i+1)
        plt.pie([sum_male_list[i], sum_female_list[i]], labels=['남성', '여성'], autopct='%1.1f%%', startangle=90)
        plt.title(city_list[i])

    plt.suptitle("대구광역시 구별 남녀 인구 비율",fontsize=25)
    plt.show()
    

    

calculate_population()














