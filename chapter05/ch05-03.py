#튜플

menu = ("돈가스", "생선가스", "우동")

print(menu, type(menu))
print(menu[0])
print(menu[1])
print(menu[2])
# menu[3] = "피자" # TypeError
# menu[2] = "자장면" # TypeError

menu += ("생선가스", ) # , 빼먹지 말것

print(menu, type(menu))

(name1, age1, hobby1) = ["홍길동", 10, "코딩"]
(name2, age2, hobby2) = ("홍길동", 10, "코딩")
print(name1, age1, hobby1)
print(name2, age2, hobby2)
