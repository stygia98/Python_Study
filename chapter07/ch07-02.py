# 지역, 전역 변수

car_total = 100

def rent(rent_count):
  global car_total
  car_total = 200
  if car_total > rent_count:
    car_total = car_total - rent_count
    print("렌트할 차량수 {} / 남은 차량수 {}" .format(rent_count, car_total))
  else:
    print("렌트 불가")
    
rent(10)
print(car_total)
