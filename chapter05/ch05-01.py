# 리스트
#===============================================
# subway = [10, 20, 30]
# subway.append(40)
# subway.remove(40)
# subway.insert(1, 100)
# subway[0] = 200
# value1 = subway.pop()
# index1 = subway.index(100)
# count1 = subway.count(100)
# # subway.clear()

# print(f"subway.pop() : [{value1}]")
# print(f"subway.index(100) : [{index1}]")
# print(f"subway.count(100) : {count1}")
# print(f"{subway} {type(subway)}")
#===============================================
# subway = ["감자", "수박", "참외"]
# subway.append("오이")
# subway.insert(1, "옥수수")
# value1 = subway.pop()
# index1 = subway.index("옥수수")
# subway[0] = "돼지감자"
# count1 = subway.count("옥수수")
# # subway.clear()

# print(f"subway.pop() : [{value1}]")
# print(f"subway.index(100) : [{index1}]")
# print(f"subway.count(100) : {count1}")
# print(f"{subway} {type(subway)}")
#===============================================
subway = [90, 10, 20, 30, 40, 60]
print(f"{subway}")
sortedsubway = sorted(subway)
print(f"{sortedsubway}")
sortedsubway = sorted(subway, reverse=True)
print(f"{sortedsubway}")

# mixList1 = [10, True, "호박", [1,2,3,4]]
# mixList2 = [20, False, "수박"]

# mixList1.extend(mixList2)
# print(f"{mixList1}")
