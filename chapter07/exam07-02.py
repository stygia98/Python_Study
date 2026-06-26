"""
Quiz) "리그 오브 레전드" 게임에서 특정 챔피언의 킬(kill), 데스(death), 어시스
트(assist) 수치를 매개변수로 받아, KDA(Kill-Death-Assist) 비율을 계산하는 함수
cal_kda를 정의하고 사용해 보세요.
힌트) (Kill + Assist)/(Death)
cal_kda(10, 2, 7)
실행결과
8.5
"""

print("=====Quiz 시작=====")

def cal_kda(kill = 0, death = 0, assist = 0):
  if death != 0:
    return float(kill + assist) / float(death)
  else:
    return float(kill + assist)

print("실행결과")
print(cal_kda(10, 2, 7))

print("=====Quiz 종료=====\n")
