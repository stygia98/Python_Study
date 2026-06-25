# if문 / match case문

# score = int(input("당신의 점수를 입력 : "))
# grade = "F"

# if 90 <= score <= 100:
#   grade = "A"
# elif 80 <= score <= 90:
#   grade = "B"    
# elif 70 <= score <= 80:
#   grade = "C"
# elif 60 <= score <= 70:
#   grade = "D"
# else:
#   grade = "F"

score = int(input("당신의 점수를 입력 : "))
grade = "F"

match score:
  # case 10 | 9:
  #   grade = "A"
  case _ if 90 <= score <= 100:
    grade = "A"
  case _ if 80 <= score <= 90:
    grade = "B"    
  case _ if 70 <= score <= 80:
    grade = "c"
  case _ if 60 <= score <= 70:
    grade = "D"
  case _ :
    grade = "F"
    
print(f"입력한 점수 : {score}\n등급 : {grade}")
