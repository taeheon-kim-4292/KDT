def create_mabang(n):
    if n % 2 == 0:
        print('홀수만을 입력하세요')
    
    mabang = [[0 for i in range(n)] for i in range(n)]
    
    # 시작 위치-> 첫 번째 행의 중앙
    y, x = 1, n // 2
    
    for num in range(1, n**2 + 1):
        mabang[y][x] = num
        
       # 다음 위치 계산
        next_y = y - 1
        next_x = x + 1
        
        # 위로 넘어가면, 맨 아래로 이동
        if next_y < 0:
            next_y = n - 1
        
        # 오른쪽으로 넘어가면, 맨 왼쪽으로 이동
        if next_x == n:
            next_x = 0
        
        # 이미 숫자가 채워진 칸을 만났을 경우
        if mabang[next_y][next_x] != 0:
            # 원래 위치에서 아래로 한 칸 이동
            next_y = y + 1
            next_x = x
            
            # 아래로 넘어갔을 경우, 맨 위로 이동
            if next_y == n:
                next_y = 0
        
        # 새 위치로 이동
        y = next_y
        x = next_x
    
    return print(mabang)



#  마방진 생성 및 출력
n = int(input("홀수차 배열의 크기를 입력하세요: "))
create_mabang(n)
