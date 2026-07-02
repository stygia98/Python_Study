# 모듈 패키지

def price(count):
  price = 14000
  print(f"인원 : {count}명 / 가격 : {price} / 총액 : {count * price}")
  
def price_morning(count):
  price = 14000 * 0.6
  print(f"인원 : {count}명 / 가격 : {price} / 총액 : {count * price}")

def price_soldier(count):
  price = 14000 * 0.3
  print(f"인원 : {count}명 / 가격 : {price} / 총액 : {count * price}")
