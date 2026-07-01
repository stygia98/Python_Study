# 예외처리

# while True:
#   try:
#     num1 = int(input("number1 >> "))
#     num2 = int(input("number2 >> "))
#     if (0 < num1 <= 10) and (0 < num2 <= 10):
#       print("{} / {} = {:.2f}" .format(num1, num2, num1/num2))
#     else:
#       raise ValueError
#   except ValueError:
#     print("오류발생")
#     continue
#   except ZeroDivisionError as e:
#     print(e)
#     continue
#   except Exception as e:
#     print(e)
#   finally:
#     print("finally")
#   break
  
# print("프로그램 종료")

# class SpecialClass():
#   def __init__(self):
#     print("생성자")
#   def __str__(self):
#     return "너무나도 더운 summer"

# sc = SpecialClass()
# print(sc)

class MyException(Exception):
  def __init__(self, message):
    self.message = message
  def __str__(self):
    return "{} 메세지 발생" .format(self.message)
  
while True:
  try:
    num1 = int(input("number1 >> "))
    num2 = int(input("number2 >> "))
    if (0 < num1 <= 10) and (0 < num2 <= 10):
      print("{} / {} = {:.2f}" .format(num1, num2, num1/num2))
    else:
      raise MyException("입력값 {} {} 범위초과" .format(num1, num2))
  except MyException as e:
    print("사용자 정의 에러")
    print(e)
    continue
  except ValueError:
    print("문자입력")
    continue
  except ZeroDivisionError as e:
    print(e)
    continue
  except Exception as e:
    print(e)
  finally:
    print("finally")
  break
