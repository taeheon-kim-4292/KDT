import csv

def get_index_of_age_csv():
    f=open(r'C:\Users\kdp\Desktop\KDT\EX_PANDAS06\data\age.csv',encoding='euc_kr')
    data = csv.reader(f)
    header = next(data)

    print('--------------------------')
    print(' age.csv index')
    print('--------------------------')

    for i in range(len(header)):
        print(f'[{i:3}]: {header[i]}')  # {i:3}: 3자리의 공간에 i값 출력\
    
    f.close()

get_index_of_age_csv()

# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib

# def draw_pie_chart(ax, city, male_count, female_count):
#     ax.pie([male_count, female_count], labels=['남', '여'], autopct='%.1f%%', 
#            startangle=90, colors=['lightblue', 'pink'], textprops={'fontsize': 8})
#     ax.set_title(city, fontsize=10)

# def calculate_population():
#     f = open(r'C:\Users\kdp\Desktop\KDT\EX_PANDAS06\data\gender.csv',encoding='euc_kr')
#     data = csv.reader(f)
#     next(data)  # header 스킵

#     city = ['대구광역시', '대구광역시 중구', '대구광역시 동구', '대구광역시 서구', 
#             '대구광역시 남구', '대구광역시 북구', '대구광역시 수성구', 
#             '대구광역시 달서구', '대구광역시 달성군', '대구광역시 군위군']

#     male_list = []
#     female_list = []

#     for row in data:
#         if '대구광역시' in row[0]:
#             for i in range(len(city)):
#                 if city[i] in row[0]:
#                     male_num = int(row[106].replace(',', ''))
#                     female_num = int(row[209].replace(',', ''))
#                     male_list.append(male_num)
#                     female_list.append(female_num)
#                     break

#     f.close()

    fig, axs = plt.subplots(5, 2, figsize=(12, 20))
    axs = axs.flatten()

    for i in range(len(city)):
        draw_pie_chart(axs[i], city[i], male_list[i], female_list[i])

    plt.tight_layout()
    plt.show()

    for i in range(len(city)):
        print(f'{city[i]}: (남:{male_list[i]:,} 여:{female_list[i]:,})')

calculate_population()



