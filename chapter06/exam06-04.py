"""
Quiz) 구구단 출력 프로그램을 만들어보자. 프로그램 사용자로부터 출력할 단
을 입력 받고, 해당 구구단을 출력하는 프로그램이다.
(for문과 while문 두가지 방식으로 구현해보자)
입력
몇 단을 출력할까요?: 5
출력
5 * 1 = 5 
5 * 2 = 10 
5 * 3 = 15 
... 
5 * 9 = 45
"""
print("=====Quiz 시작=====")

print("입력")
mulTable = int(input("몇 단을 출력할까요? : "))

print("\nfor문 출력")
for i in range(1, 10):
  print(f"{mulTable} * {i} = {mulTable * i}")

print("\nwhlie문 출력")
i = 0
while i < 9:
  i = i + 1
  print(f"{mulTable} * {i} = {mulTable * i}")

print("=====Quiz 종료=====\n")
