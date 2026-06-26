"""
Quiz) 표준 체중을 구하는 프로그램을 작성하시오
* 표준 체중 : 각 개인의 키에 적당한 체중
(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
함수명 : std_weight
전달값 : 키(height), 성별(gender) 

조건2 : 표준 체중은 소수점 둘째자리까지 표시
(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
"""
print("=====Quiz 시작=====")

height = float(input("키(cm) : "))
gender = input("성별 (M/F) : ").upper()

def std_weight(height, gender):
  if height > 3: height = height/100
  
  if gender == "M":
    return height * height * 22
  elif gender == "F":
    return height * height * 21
    
weight = std_weight(height, gender)
gender = "남자" if gender == "M" else "여자"

print(f"키 {height:.0f}cm {gender}의 표준 체중은 {weight:.2f}kg 입니다")

print("=====Quiz 종료=====\n")
