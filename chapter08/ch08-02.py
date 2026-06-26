# 파일입출력

# 파일 쓰기

# file_handle = open("score.txt", "w", encoding="UTF-8")
# print("국어 : 90", file = file_handle)
# print("수학 : 100", file = file_handle)
# print("영어 : 100", file = file_handle)
# file_handle.close()

# file_handle = open("score.txt", "a", encoding="UTF-8")
# print("자바 : 90", file = file_handle)
# print("파이썬 : 100", file = file_handle)
# file_handle.close()

# file_handle = open("score.txt", "a", encoding="UTF-8")
# file_handle.write("HTML : 100\n")
# file_handle.write("CSS : 90\n")
# file_handle.close()

#파일 읽기

# file_handle = open("score.txt", "r", encoding="UTF-8")
# print(type(file_handle))
# print(file_handle.read())
# print(file_handle.readline(), end="")
# file_handle.close()



# file_handle = open("score.txt", "r", encoding="UTF-8")
# exit_Flag = False

# while not exit_Flag:
#   line = file_handle.readline()
#   if not line:
#     print("EOF")
#     exit_Flag = True
#   else:
#     print(line, end="")
  
# file_handle.close()



# file_handle = open("score.txt", "r", encoding="UTF-8")
# f_List = file_handle.readlines()
# file_handle.close()

# print(f_List, type(f_List))
# for data in f_List:
#   print(data, end="")
