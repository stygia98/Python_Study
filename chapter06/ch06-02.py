# 반복문

# list = [1, 3, 5, 7, 9]

# for no in list:
#   print("{} " .format(no), end="")

# print()
# for no in [1, 3, 5, 7, 9]:
#   print("{} " .format(no), end="")

# print()
# for no in range(1, 10, 2):
#   print("{} " .format(no), end="")

# orders = ["햄버거", "자장면", "짬뽕"]
# print()
# for data in orders:
#   print("{} " .format(data), end="")



# students = [1, 2, 3, 4, 5]
# # students = [11, 12, 13, 14, 15]
# print()
# students = [ no * 10 for no in students ]
# print(students)



# menu = ["햄버거", "자장면", "짬뽕"]
# print(menu)
# menu1 = [ data for data in menu ]
# print(menu1)

# like_subject = ["Java", "Python", "Html", "JavaScript", "Spring Boot"]
# like_subject1 = [ subject.upper() for subject in like_subject ]
# print(like_subject)
# print(like_subject1)



# count = 0
# exitFlag = False

# while not exitFlag:
#   count += 1
#   print("count = {}" .format(count))
#   if count >= 100:
#     exitFlag = True



data_list = [1, 2, 3, 4, 5]
no = int(input("[1,2,3,4,5] 선택입력 : "))

# for i in data_list:
#   if no == i:
#     print("있어요")
#     break
#   else:
#     print("없어요")

if no in data_list : 
  print("있어요")
else:
  print("없어요")