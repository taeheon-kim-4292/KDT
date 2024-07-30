import	csv
import	matplotlib.pyplot as	plt
import	platform
import	math
import	koreanize_matplotlib

def calculate_population():
    f = open(r'C:\Users\kdp\Desktop\KDT\EX_PANDAS06\data\gender.csv',encoding='euc_kr')
    data=csv.reader(f)
    male_list=[]
    female_list=[]
    bubble_size_list=[]
    city=['대구광역시', '대구광역시 중구', '대구광역시 동구', '대구광역시 서구', 
            '대구광역시 남구', '대구광역시 북구', '대구광역시 수성구', 
          '대구광역시 달서구', '대구광역시 달성군', '대구광역시 군위군']

    for row in data:
        if '대구광역시 중구' in row[0]:
            for i in range(106,207):
                male_num = int(row[i].replace(',',''))
                female_num = int(row[i+103].replace(',',''))
                # 버블의 사이즈 조절
                bubble_size_list.append(math.sqrt(male_num+female_num))
                male_list.append(male_num)
                female_list.append(female_num)
            break
    f.close()
    print(f'대구광역시 중구: (남:{sum(male_list)} 여:{sum(female_list)})')
calculate_population()