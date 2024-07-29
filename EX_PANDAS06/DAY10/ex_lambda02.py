class Student:
    def __init__(self, name, grade, number):
        self.name = name
        self.grade = grade
        self.number = number

    def __repr__(self):
        return f'({self.name}, {self.grade}, {self.number})'    # 객체를 문자열로 표현하는 함수

#  Student 객체 리스트 생성
students = [Student('홍길동', 3.9, 20240303),
           Student('김유신',3.0,20240302),
           Student('박문수', 4.3, 20240301)]

print(students[0])  # Student 객체 출력: Student 클래스에 __repr__()에 정의된 형태로 출력

sorted_list = sorted(students, key=lambda s:s.name)
print(sorted_list)