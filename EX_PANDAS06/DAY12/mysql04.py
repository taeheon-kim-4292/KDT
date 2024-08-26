import	pymysql
conn=pymysql.connect(host='localhost',	user='root',	password='4292',
db='sqlclass_db',	charset='utf8')

curs=conn.cursor()
sql = """ insert into customer(name,category,region)
          values(%s, %s, %s)"""

curs.execute(sql, ('홍길동',1,'서울'))
curs.execute(sql, ('이연수',2,'서울'))      # customer 테이블에 데이터추가 -> 반드시 commint() 함수 호출
conn.commit()

print('Insert  완료')

curs.execute('select * from customer')
rows = curs.fetchall()  # 모든 데이터를 가져옴
print(rows)

curs.close()
conn.close()     # database 종료
