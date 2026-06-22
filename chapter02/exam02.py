
"""
Quiz) 변수를 이용하여 다음 문장을 출력하시오
변수명 : station
변수값 : "사당", "신도림", "인천공항" 순서대로 입력
출력 문장 : XX 행 열차가 들어오고 있습니다.
"""

print("=====Quiz 1 시작=====")
for i in range(0, 3) :
  station = input("역 이름 입력 >> ")
  print(station + " 행 열차가 들어오고 있습니다.")
print("=====Quiz 1 종료=====\n")

"""
# Quiz)다음 챔피언의 정보를 변수에 저장하고 출력해보세요.
# 이름 - 유미
# 레벨 - 6
# 체력 - 950
# 대사 - 나랑 유미랑!
"""

# name = input("이름 입력 >> ")
# lvl = input("레벨 입력 >> ")
# hpPoint = input("체력 입력 >> ")
print("=====Quiz 2 시작=====")
name = "유미"
lvl = 6
hpPoint = 950
script = "나랑 유미랑!"
print("이름 - " + name) 
print("레벨 - " + str(lvl)) 
print("체력 - " + str(hpPoint)) 
print("대사 - " + script) 
print("=====Quiz 2 종료=====\n")

"""
Quiz)포켓몬이름을 사용자로부터 입력 받아서 메시지를 완성해 봅시다.
입력
파이리
출력
받아라 몬스터볼~! 파이리 넌 내꺼야!
힌트> name = input(“이름을 입력”)
"""

print("=====Quiz 3 시작=====")
name = input("이름 입력 >> ")
print("출력")
print("받아라 몬스터볼~! " + name + " 넌 내꺼야! ")
print("=====Quiz 3 종료=====\n")
