import	csv
import	matplotlib.pyplot as	plt
import	re
import	koreanize_matplotlib
def	parse_district_name(city):
				'''
				'행정구역'	명칭에서 숫자 부분을 제거함
                - 서울특별시 종로구 (1111000000)
				'''
				city_name =	re.split('[()]',	city)
				#print(city_name)
				return	city_name[0]
def	print_population(population):
	'''
	특정 지역의 인구 현황을 화면에 출력함
    '''
	for	i in range(len(population)):
		print(f'{i:3d}세:	{population[i]:4d}명',	end='	')
		if	(i +	1)	%	10	==	0:
			    print()