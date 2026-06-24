"""
Quiz) 게임에서 플레이어가 얻은 점수들을 가진 scores 리스트가 있다. 가장 높은 점
수를 찾는 프로그램을 작성해 보세요. scores = [120, 150, 180, 200, 170] 
힌트) max_score 변수를 하나 생성해 준다.
실행결과
최고점수 : 200
"""
print("=====Quiz1 시작=====")
scores = [120, 150, 180, 200, 170]
max_score = sorted(scores)
print(f"{max_score}")
print(f"최고점수 : {max_score.pop()}")
print("=====Quiz1 종료=====\n")

# max_score1 = scores[0]
# for score in scores :
#   if max_score1 < score :
#     max_score1 = score
# print(f"최고점수 : {max_score1}")


"""
Quiz)게임에서 각 방에 숨겨진 아이템 개수를 나타내는 2차원 리스트가 있다. 모든
방을 돌아다니며 아이템을 수집하는 프로그램을 작성하세요. 아이템이 없는 방은 0
으로 표시된다.
rooms = [ [3, 1, 2], [2, 0, 1], [1, 3, 2] ] 
힌트) sum(리스트)는 리스트의 합계를 계산해 준다.
for room in rooms:
total += sum(room)
실행결과
총 수집한 아이템 수 : 15
"""

print("=====Quiz2 시작=====")
rooms = [ [3, 1, 2], [2, 0, 1], [1, 3, 2] ] 
total = 0
for i in range(0, 3):
  for j in range(0, 3):
    total += rooms[i][j]
    
print(f"{rooms}")
print(f"총 수집한 아이템 수 : {total}")
print("=====Quiz2 종료=====\n")

# total2 = 0
# for i in range(0, 3):
#     total2 += sum(rooms[i])
# print(f"총 수집한 아이템 수 : {total2}")

# total3 = 0
# for room in rooms:
#   total3 += sum(room)
# print(f"총 수집한 아이템 수 : {total3}")

# total4 = 0
# for room in rooms :
#   total4 += sum(room)
#   print(f"{room}의 합{sum(room)}")
# print(f"{rooms}의 총합은 {total4}")

# total5 = 0
# for room in rooms :
#   for data in room :
#     total5 += data
# print("{}의 총합은{}" .format(rooms, total5))
