# # Dict 전용 함수 즉, 매서드
# # -> keys(), values(), items()
person={'name':'홍길동', 'age':10}

# # # 메서드 - 값 읽어오는 메서드 get(key,default)
# # # - key에 해당하는 value가 없으면 default
print(person['name'])
#print(person['gender'])     # KeyError

print(person.get('name'))
print(person.get('gender','없음'))
print(person.get('gender'))
# 메서드 - 수정 및 업데이트 
# 수정/업데이트
person['gender']='여'
person.update({'gender':'어린이','job':'학생'})
print(person)

person.update({'phone':'010','birth':'991025'})
print(person)

##  **{'weight':100,'height':'10'}) ==> weight=100, height=170  ????????????????????????????????
person.update( **{'weight':100,'height':'10'})
print(person)

# msg="Hello Good Luck"
# alpha=set(msg)
# save={}
# for m in alpha:
#     print(m,msg.count(m))
#     save[m]=msg.count(m)

# print(sorted(save))