import pandas as pd
from tabulate import tabulate

# 지하철 시간대별 이용현호나
df = pd.read_excel(r'C:\Users\kdp\Desktop\KDT\EX_PANDAS06\subway.xls',sheet_name='지하철 시간대별 이용현황',header=[0,1])
# print(df.head())
# print(df.columns)
# print(df[('지하철역','Unnamed: 3_level_1')])
commute_time_df = df.iloc[:,[1,3,10,12,14]]
# print(commute_time_df.dtypes)
commute_time_df[('07:00:00~07:59:59',	'승차')] = commute_time_df[('07:00:00~07:59:59',	'승차')].apply(lambda x:x.replace(',',''))
commute_time_df[('08:00:00~08:59:59',	'승차')] = commute_time_df[('08:00:00~08:59:59',	'승차')].apply(lambda x:x.replace(',',''))
commute_time_df[('09:00:00~09:59:59',	'승차')] = commute_time_df[('09:00:00~09:59:59',	'승차')].apply(lambda x:x.replace(',',''))
print(tabulate(commute_time_df.head(),headers='keys', tablefmt='psql'))

commute_time_df= commute_time_df.astype({('07:00:00~07:59:59',	'승차'):'int64'})
commute_time_df= commute_time_df.astype({('08:00:00~08:59:59',	'승차'):'int64'})
commute_time_df= commute_time_df.astype({('09:00:00~09:59:59',	'승차'):'int64'})

row_sum_df = commute_time_df.sum(axis=1, numeric_only=True)
passenger_number_list = row_sum_df.to_list()
print(row_sum_df)

max_number =row_sum_df.max(axis=0)	#	해당 열에서 최대값 찾기
print(max_number)

max_index =	row_sum_df.idxmax()
max_line,	max_station =	df.iloc[max_index,	[1,	3]]	#최대값의 [1]:	호선,[3]:	지하철역명
print(f'출근 시간대 최대 승차 인원역:	{max_line}	{max_station}, 하차인원: {max_number:,}명')