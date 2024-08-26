import pymysql
import pandas as pd
import csv

import pymysql.cursors

# # cursor.description 속성
# conn = pymysql.connect(host='localhost', user='root', password='4292',
#                        db='sakila', charset='utf8')
# cur=conn.cursor()
# cur.execute('select * from language')
# desc=cur.description    # 헤더 정보를 가져옴
# for i in range(len(desc)):
#     print(desc[i][0], end=' ')
# print()

# rows=cur.fetchall() # 모든 데이터를 가져옴
# for data in rows:
#     print(data)
# print()

# cur.close()
# conn.close()    # 데이터베이스 연결종료


conn = pymysql.connect(host='localhost', user='root', password='4292',
                       db='sakila', charset='utf8')
cur=conn.cursor(pymysql.cursors.DictCursor)
cur.execute('select * from language')
rows = cur.fetchall() # 모든 데이터를 가져옴
print(rows)

language_df=pd.DataFrame(rows)
print(language_df)
print()
print(language_df['name'])
cur.close()
conn.close()    # DB 연결종료