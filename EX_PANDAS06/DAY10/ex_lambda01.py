# key 매개변수에 lambda식 사용
        # 이름 학점 학번

students=[('Alice', 3.9, 20160303),
          ('Charlie',4.3,20160301),
          ('Bob',3.0,20160302)]

print('-'*50)
print('sorted key 입력 없음')
print(sorted(students))

# 학번(students[2])을 기준으로 오름차순 정렬
print('학번 기준 오름차순 정렬')
sorted_students1 = sorted(students, key = lambda s:s[2])
print(sorted_students1)

# 학점(students[1])을 기준으로 내림 차순 정렬
print('학점 기준 내림차순 정렬')
sorted_students2 = sorted(students, key = lambda s: s[1], reverse=True)
print(sorted_students2)

