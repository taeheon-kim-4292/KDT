import pymysql

def create_table(conn,cur):
    try:
        query1 = "drop table if exists customer"
        query2 = """
            create table customer
            (name varchar(10),
            category smallint,
            region varchar(10))
        """
        cur.execute(query1)
        cur.execute(query2)
        conn.commit()
        print('Table 생성완료')
    except Exception as e:
        print(e)

def main():
    conn = pymysql.connect(host='localhost', user='root', password='4292',
                       db='sqlclass_db', charset='utf8')
    
    cur = conn.cursor()

    # 테이블 생성 함수 호출
    create_table(conn,cur)

    # 연결종료
    cur.close()
    conn.close()
    print('DataBase 연결종료')
main()