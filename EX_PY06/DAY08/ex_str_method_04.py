# 문자열에서 원소/요소 변경해주는 메서드 -> replace()
msg='Pithon'

# 인덱스로 요소 변경
# msg[1]='y'      # ERROR 미지원 기능: 불변의 시퀀스 타입

# 전용 메서드로 변경
m1=msg.replace('i','y')
print(f'msg: {msg} ---> m1 : {m1}')

# 변경 적용 위해서는 반드시 저장!!
msg=msg.replace('i','y')

msg="Good Happy"
# - o ==> O로 변경
print(msg.replace('o','O'))

# - o ==> 0로 1개만 변경
print(msg.replace('o','O',1))