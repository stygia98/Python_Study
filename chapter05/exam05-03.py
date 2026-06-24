"""
Quiz) 여러 회사의 주식 정보가 다음과 같은 형식으로 저장되어 있다. 각 회사별로 '
최고가'와 '최저가'를 출력하는 프로그램을 작성하세요.
stocks_info = {
'삼성전자': {'최고가': 85000, '최저가': 80000, '현재가': 82000},
'SK하이닉스': {'최고가': 145000, '최저가': 139000, '현재가': 140500},
'네이버': {'최고가': 360000, '최저가': 340000, '현재가': 350000}
}
실행결과
삼성전자 - 최고가: 85000, 최저가: 80000 SK하이닉스 - 최고가: 145000, 최저가: 
139000 네이버 - 최고가: 360000, 최저가: 340000
"""

stocks_info = {
'삼성전자': {'최고가': 85000, '최저가': 80000, '현재가': 82000},
'SK하이닉스': {'최고가': 145000, '최저가': 139000, '현재가': 140500},
'네이버': {'최고가': 360000, '최저가': 340000, '현재가': 350000}
}

# value1 = 0
# value2 = 0
# for value1 in stocks_info.values():
#   # print(value1)
#   # print(value1.values())
#   max_value = value2
#   min_value = 999999999
#   for value2 in value1.values():
#     # print(value2)
#     if max_value < value2:
#       max_value = value2
#     if min_value > value2:
#       min_value = value2
#   print(f"최고가 : {max_value} / 최저가 : {min_value}")
  
# for key1 in stocks_info.keys():
#   value3 = stocks_info[key1]
#   # print(value3)
#   # for key2 in stocks_info.keys():
#   # print(value3["최고가"] )
#   print(f"{key1} - 최고가 : {value3['최고가']}, 최저가 : {value3['최저가']}")
  
for key1, value1 in stocks_info.items():
  # print(key1, value1)
  print(f"{key1} - 최고가 : {value1['최고가']}, 최저가 : {value1['최저가']}")
  # for key2, value2 in value1.items():
    # print(key2, value2)