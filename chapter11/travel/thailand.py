# 모듈 패키지

class ThailandModule:
  # def __ini__(self) #defult
  def detail_travel(self):
    print("태국 여행 : 가격 60만원")

if __name__ == "__main__":
  print("ThailandModule 내부 호출 중")
  test_obj = ThailandModule()
  test_obj.detail_travel()
else: 
  print("모듈 외부 호출 중")
