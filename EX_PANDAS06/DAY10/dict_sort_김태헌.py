def print_menu():
    print("-----------------------------------------")
    print("1. 전체 데이터 출력")
    print("2. 수도 이름 오름차순 출력")
    print("3. 모든 도시의 인구수 내림차순 출력")
    print("4. 특정 도시의 정보 출력")
    print("5. 대륙별 인구수 계산 및 출력")
    print("6. 프로그램 종료")
    print("-----------------------------------------")
print_menu()

 
# 1번
def print_dict(dict):
    for key, values in dict.items():
        print(f"{key}: {values}")

# 2번
def sort_dict(dict):
    for city in sorted(dict):
        print(f"{city}: {dict[city]}")

# 3번
def sort_pop_down(dict):
    sort1 = sorted(dict.items(), key=lambda x: x[1][2], reverse=True)
    idx=0
    for city,values in sort1:
        idx=idx+1
        print(f"[{idx}]{city:15}: {values[2]:,}")


# 4번

def city_info(dict, city_name):
    if city_name in dict:
        print(f"도시:{city_name}\n국가: {dict[city_name][0]}, 대륙:{dict[city_name][1]}, 인구수:{dict[city_name][2]:,}")
    else:
        print(f"도시이름: {city_name}은 key에 없습니다.")
# 5번

def sort_pop(dict,continent_name):
    total_pop=0
    for city, values in dict.items():
        if values[1] == continent_name:
            print(f"{city}: {values[2]:,}")
            total_pop += values[2]
    print(f"{continent_name}   전체 인구수: {total_pop:,}")


def main():
    dict = {
        'Seoul': ['South Korea', 'Asia', 9655000],
        'Tokyo': ['Japan', 'Asia', 14110000],
        'Beijing': ['China', 'Asia', 21540000],
        'London': ['United Kingdom', 'Europe', 14800000],
        'Berlin': ['Germany', 'Europe', 3426000],
        'Mexico City': ['Mexico', 'America', 21200000]}
    while True:
        print_menu()
        choice = input("메뉴를 입력하세요: ")

        if choice == '1':
            print_dict(dict)
        elif choice == '2':
            sort_dict(dict)
        elif choice == '3':
            sort_pop_down(dict)
        elif choice == '4':
            city_name = input( '원하시는 도시명을 입력하세요: ')
            city_info(dict,city_name)
        elif choice == '5':
            continent_name = input("대륙 이름을 입력하세요(Asia, Europe, America): ")
            sort_pop(dict,continent_name)
        elif choice == '6':
            print('프로그램을 종료합니다.')
            break
        else:
            continue

if __name__ == "__main__":
    main()