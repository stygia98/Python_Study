# 함수
# def add_func(num1, num2):
#   print("덧셈 함수")
#   return num1 + num2

# sum = add_func(10, 20)

# print(f"결과값 : {sum}")



def profile(name, age = 20, main_subject = "Java"):
  print("이름 : {}, 나이 : {}, 언어 :{}" .format(name, age, main_subject))    

profile("홍길동1", 18, "C++")
profile("홍길동2")

def new_profile1(name, age, lang1, lang2, lang3):
  print(name, age, lang1, lang2, lang3)

def new_profile2(name, age, *lang):
  print(name, age)
  print(lang, type(lang))
  for langtemp in lang:
    print("{} " .format(langtemp), end="")

new_profile2("홍길동1", 18, "C", "C++", "Java", "Spring", "A", "B", "C")
