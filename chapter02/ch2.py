#자료형 - 숫자
# print(5)
# print(-5)
# print(3.141592)
# print(-3.141592)

#연산자 - (+, -, *, /, %, //)
# print(5+5)
# print(2*8)
# print(6/4)
# print(6%4)
# print(6//4)
# print(4*6/3)

#문자열
# print("여름과일" + "수박")
# print("당신의 나이는 : " + str(23))
# print(int("54") + 24)
# print("&" * 10)
# print('오렌지', '토마토')
# print('파이썬')
# print("오늘은 \"정말로\" 공부를 열심히 했습니다.")

#boolean
# print(10 > 5)
# print(10 < 5)
# print(True)
# print(False)
# print(not (10 >5))

#변수
# print("길동씨 당신이 좋아하는 동물은 무엇입니까?")
# print("내가 좋아하는 동물은 개입니다, 그리고 이름은 해피입니다.")
# print("해피의 나이는 4살이구요, 산책을 좋아합니다")

# name = "길동"
# animal = "고양이"
# animalName = "뽀삐"
# animalAge = 3
# animalHobby = "먹는것"

# print(name + "씨 당신이 좋아하는 동물은 무엇입니까?")
# print("내가 좋아하는 동물은 " + animal + "입니다, 그리고 이름은 " + animalName + "입니다.")
# print(animalName + "의 나이는 " + str(animalAge) + "살이구요, " + animalHobby + "을 좋아합니다")

#타입변환
# print(int("3") + 4)
# print(float("3.5") + 4.2)
# print(int(3.5))
# #print(int("삼")) # ValueError: invalid literal for int() with base 10: '삼'

# type 확인
# print(type(3))
# print(type("3"))
# print(type('str'))
# print(type("string"))
# print(type(3.5))
# print(type(True))
# print(type(str(3)))

# age = 10
# print(type(age))
# age = age > 20
# print(type(age))

# anotation1
""" anotation2 """
''' anotation3 '''

for i in range(0,3) :
  name = input("당신의 이름 >> ")
  print("당신의 이름은 " + name + " 입니다.")
print("연습문제 종료")
