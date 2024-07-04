# [18.5]
# 0~73 사이의 숫자 중 3으로 끝나는 숫자 출력
# 3 13 23 33 43 53 63 73 => 10으로 나누었을 때 나머지 3
i = 0
while True:
    if i >73: break
    i=i+1
    if i%10 !=3:
        continue
    print(i,end=' ')

