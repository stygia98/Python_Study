#입출력

# inputText = input("입력 : ")
# print(inputText, type(inputText)) #int, float, boolean <-> str



# age = float(input("나이입력 >> "))
# print("나이는 {}" .format(age))
# print(f"나이는 {age}")

# print("파이썬", "자바", "자바스크립트", "스프링부트", sep=", ", end="end")

# import sys
# print("파이썬", "자바", file=sys.stdout)
# print("파이썬", "자바", file=sys.stderr)




# scores = {"국어": 70, "수학": 100, "영어": 90}

# for key in scores.keys():
#   print("key : {}" .format(key))

# for value in scores.values():
#   print("value : {}" .format(value))
  
# for key, value in scores.items():
#   # print("key : {} / value : {}" .format(key, value))
#   print(key.ljust(3), str(value).rjust(3), sep="/")
  


# for i in range(1, 8):
#   print("num : "+ str(i).zfill(3))
  
  
  
print("{1} {0}" .format(100, 200))
print("{0: >10}" .format(100))
print("{0:_>10}" .format(100))
print("{0:_>+10}" .format(100))

print("{0:,}" .format(100000000000))
print("{0:+,}" .format(100000000000))
print("{0:+,}" .format(-100000000000))

print("{0:_>+30,}" .format(-100000000000))

print("{0:10.2f}" .format(95.7867))
