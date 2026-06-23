#문자열
# message = "파이썬을 공부하고 있습니다"
# print(message, type(message))

# message2 = """
# 파이선을
# 공부
# 하고 있습니다
# """
# print(message, type(message))

#slice
# idNum = "990229-1234567"

# no = idNum[7]
# print(type(no))
# print("사용자 연도 : ", idNum[0:2])
# print("사용자 월 : ", idNum[2:4])
# print("사용자 일 : ", idNum[4:6])
# print("사용자 성별번호 : ", idNum[7])
# print("사용자 생년월일 : ", idNum[0:6])
# print("주민번호 뒷자리 : ", idNum[7:])
# print("주민번호 검증번호제외 : ", idNum[7:-1])
# print("주민번호 문자열길이 : ", len(idNum))

# for i in range(0, len(idNum)):
#   if idNum[i] == "-" :
#     continue
#   print(idNum[i], end=" ")

#문자열 처리 함수

# message = "Python is amazing"

# print(message.lower())
# print(message.upper())
# print(message.isupper())
# print(message[0].isupper())
# print(message[1:3].islower())
# print(message.count("n"))
# print(message.count("k"))
# print(len(message))
# print(message.replace("Python", "Java"))

# 차이점 / find() index()
# indIndex = message.find("n")
# print(findIndex)
# findIndex2 = message.find("n", findIndex+1)
# print(findIndex2)
# findIndex3 = message.find("is")
# print(findIndex3)

# findIndex4 = message.find("Java") # -1
# print(findIndex4)
# findIndex5 = message.index("Java") # VlaueError
# print(findIndex5)

# findIndex6 = message.find("n", 6, -1)
# print(findIndex6)
# findIndex7 = message.index("n", 6, -1)
# print(findIndex7)

# 문자열포맷
# age = 20
# print("나는 %d살 입니다." %age)
# like = "Python"
# print("나는 %s을 좋아합니다." %like)
# score = 96.50
# print("점수는 : %.2f" %score)
# flag = True
# print("참?거짓? : %s" %flag)
# fruit1 = "수박" 
# fruit2 = "참외"
# print("좋아하는 과일 : %s, %s" %(fruit1, fruit2))

# age = 20
# print("나는 {}살 입니다." .format(age))
# like = "Python"
# print("나는 {}을 좋아합니다." .format(like))
# score = 96.50
# print("점수는 : {}" .format(score))
# flag = True
# print("참?거짓? : {}" .format(flag))
# fruit1 = "수박" 
# fruit2 = "참외"
# print("좋아하는 과일 : {1}, {0}" .format(fruit1, fruit2))

# age = 20
# print(f"나는 {age}살 입니다.")
# like = "Python"
# print(f"나는 {like}을 좋아합니다.")
# score = 96.50
# print(f"점수는 : {score}")
# flag = True
# print(f"참?거짓? : {flag}")
# fruit1 = "수박" 
# fruit2 = "참외"
# print(f"좋아하는 과일 : {fruit1}, {fruit2}")

#탈출문자
print("파이썬\n자바")
print("파이썬\t자바")
print("파이썬\b자바")
print("파이썬\r자바")
print("D:\\JAVA_test\\.metadata\\.mylyn")
