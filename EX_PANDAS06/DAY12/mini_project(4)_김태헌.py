import pymysql
import pandas as pd
import numpy as np
# 모듈 준비
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
# 한글 폰트 설정 ->폰트 매니저 모듈
from matplotlib import font_manager as fm
from matplotlib import rc
import seaborn as sns 

# conn=pymysql.connect(host='172.20.145.81',user='taeheon',
#                      password='1234', db='mini_project')

# cur = conn.cursor()
# cur.execute('select * from Starbucks_Country')
# rows=cur.fetchall()     # 모든 데이터를 가져옴
# print(rows)

# Starbucks_df = pd.DataFrame(rows)
# print(Starbucks_df)

# cur.close()


conn=pymysql.connect(host='172.20.145.81',user='taeheon',
                     password='1234', db='mini_project')

cur = conn.cursor()

query = """
select st.Country,st.latte,st.expensive,g.Year_2022 
from Starbucks_Country as st
    inner join gdp_data as g
    on st.Country = g.Country  """
cur.execute(query)
rows=cur.fetchall()
for row in rows:
    print(row)

stargdp_df=pd.DataFrame(row)
print(type(stargdp_df))
cur.close()
conn.close()
