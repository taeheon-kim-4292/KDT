# 함수명에 대해서
# -> 코드가 있는 부분에 붙여진 이름
# -> 코드가 시작되는 주소를 저장하고 있음
# [내장함수]
show=print

show("Happy")

# 함수명 여러개를 리스트에 담아서 원소로 처리 ---------------
datas=[11,22,33]
func=[max,min,sum]
print(func[0](datas),func[1](datas),func[2](datas))