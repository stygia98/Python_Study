#딕셔너리(key value)

cabinet = {3: "푸", 100: "피글렛", 3: "푸2", 4: "피글렛"}

# cabinet[5] = "쿠우"
# del cabinet[5]

# print(3 in cabinet)
# print('피글렛' in cabinet.values())
# print(cabinet)

# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())

keylist = cabinet.keys()
for key in keylist :
  print(cabinet[key])
