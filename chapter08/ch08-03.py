# pickle

import pickle

# 파일 생성
# profile_handle = open("profile.pickle", "wb")

# profile_dic = {"이름":"홍길동1", "나이":18, "취미":["등산", "배드민턴", "탁구"]}
# pickle.dump(profile_dic, profile_handle)



#파일 출력
# print(profile_dic, type(profile_dic))

# for key, item in profile_dic.items():
#   print(key, item)

# profile_handle.close()



#pickle 사용
# profile_handle = open("profile.pickle", "rb")
# list_dic = pickle.load(profile_handle)
# profile_handle.close()

# print(list_dic, type(list_dic))

# for key, item in list_dic.items():
#   print(key, item)


# with문 (try catch)

# with open("profile.pickle", "rb") as profile_handle:
#   list_dic = pickle.load(profile_handle)
#   for key, value in list_dic.items():
#     print(key, value)
#     if key == "취미":
#       for data in value:
#         print("{} = {}" .format(key, data))
    
# print("with # profile_handle.close() - do not need to close()")



# with open("data.txt", "w", encoding="UTF-8") as data_handle:
#   data_handle.write("파이썬\n")
#   data_handle.write("자바\n")
#   data_handle.write("스프링부트\n")

with open("data.txt", "r", encoding="UTF-8") as data_handle:
  print(data_handle.read())
