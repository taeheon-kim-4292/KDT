import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
# 한글 폰트 설정 ->폰트 매니저 모듈
from matplotlib import font_manager as fm
from matplotlib import rc

# 적용할 폰트 파일
font_file=r'C:\Windows\Fonts\batang.ttc'

# 폰트 패밀리
font_name= fm.FontProperties(fname=font_file).get_name()

# 새로운 폰트 패밀리 이름 지정
rc('font', family=font_name)

# set_custonFont(r'C:\Windows\Fonts\batang.ttc')
# 지하철 시간대별 이용현황
df = pd.read_excel(r'C:\Users\kdp\Desktop\KDT\EX_PANDAS06\subway.xls',sheet_name='지하철 시간대별 이용현황',header=[0,1])
print(df.columns)
print(df[('지하철역','Unnamed: 3_level_1')])

commute_time_df = df.iloc[:,[1,3,11,13]]
print(commute_time_df.dtypes)
commute_time_df.columns = ['호선명', '지하철역', '07:00:00~07:59:59_하차', '08:00:00~08:59:59_하차']

commute_time_df[('07:00:00~07:59:59_하차')] = commute_time_df[('07:00:00~07:59:59_하차')].apply(lambda x:x.replace(',',''))
commute_time_df[('08:00:00~08:59:59_하차')] = commute_time_df[('08:00:00~08:59:59_하차')].apply(lambda x:x.replace(',',''))
print(tabulate(commute_time_df.head(40),headers='keys', tablefmt='psql'))

commute_time_df= commute_time_df.astype({('07:00:00~07:59:59_하차'):'int64'})
commute_time_df= commute_time_df.astype({('08:00:00~08:59:59_하차'):'int64'})

# 출근 시간대 총 하차 인원 계산
commute_time_df['하차 인원'] = commute_time_df['07:00:00~07:59:59_하차'] + commute_time_df['08:00:00~08:59:59_하차']


# 1호선 최대 하차 인원 찾기
line_1 = commute_time_df[commute_time_df['호선명'] == '1호선']
max_index_1 = line_1['하차 인원'].idxmax()
max_station_1 = line_1.loc[max_index_1]
print(f'출근 시간대 1호선 최대 하차역: {max_station_1["지하철역"]}, 하차인원: {max_station_1["하차 인원"]:,}명')

# 2호선 최대 하차 인원 찾기
line_2 = commute_time_df[commute_time_df['호선명'] == '2호선']
max_index_2 = line_2['하차 인원'].idxmax()
max_station_2 = line_2.loc[max_index_2]
print(f'출근 시간대 2호선 최대 하차역: {max_station_2["지하철역"]}, 하차인원: {max_station_2["하차 인원"]:,}명')

# 3호선 최대 하차 인원 찾기
line_3 = commute_time_df[commute_time_df['호선명'] == '3호선']
max_index_3 = line_3['하차 인원'].idxmax()
max_station_3 = line_3.loc[max_index_3]
print(f'출근 시간대 3호선 최대 하차역: {max_station_3["지하철역"]}, 하차인원: {max_station_3["하차 인원"]:,}명')

# 4호선 최대 하차 인원 찾기
line_4 = commute_time_df[commute_time_df['호선명'] == '4호선']
max_index_4 = line_4['하차 인원'].idxmax()
max_station_4 = line_4.loc[max_index_4]
print(f'출근 시간대 4호선 최대 하차역: {max_station_4["지하철역"]}, 하차인원: {max_station_4["하차 인원"]:,}명')

# 5호선 최대 하차 인원 찾기
line_5 = commute_time_df[commute_time_df['호선명'] == '5호선']
max_index_5 = line_5['하차 인원'].idxmax()
max_station_5 = line_5.loc[max_index_5]
print(f'출근 시간대 5호선 최대 하차역: {max_station_5["지하철역"]}, 하차인원: {max_station_5["하차 인원"]:,}명')

# 6호선 최대 하차 인원 찾기
line_6 = commute_time_df[commute_time_df['호선명'] == '6호선']
max_index_6 = line_6['하차 인원'].idxmax()
max_station_6 = line_6.loc[max_index_6]
print(f'출근 시간대 6호선 최대 하차역: {max_station_6["지하철역"]}, 하차인원: {max_station_6["하차 인원"]:,}명')

# 7호선 최대 하차 인원 찾기
line_7 = commute_time_df[commute_time_df['호선명'] == '7호선']
max_index_7 = line_7['하차 인원'].idxmax()
max_station_7 = line_7.loc[max_index_7]
print(f'출근 시간대 7호선 최대 하차역: {max_station_7["지하철역"]}, 하차인원: {max_station_7["하차 인원"]:,}명')


x_labels = [f'1호선 {max_station_1["지하철역"]}', f'2호선 {max_station_2["지하철역"]}', f'3호선 {max_station_3["지하철역"]}', 
            f'4호선 {max_station_4["지하철역"]}', f'5호선 {max_station_5["지하철역"]}', f'6호선 {max_station_6["지하철역"]}', 
            f'7호선 {max_station_7["지하철역"]}']
y_values = [max_station_1["하차 인원"], max_station_2["하차 인원"], max_station_3["하차 인원"], 
            max_station_4["하차 인원"], max_station_5["하차 인원"], max_station_6["하차 인원"], 
            max_station_7["하차 인원"]]

plt.figure(figsize=(10, 6))
plt.bar(x_labels, y_values, color='blue')
plt.xlabel('호선 + 지하철 역 이름')
plt.ylabel('')
plt.title('출근 시간대 지하철 노선별 최대 하차역')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()