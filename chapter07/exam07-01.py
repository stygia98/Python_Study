"""
Quiz) "리그 오브 레전드" 게임에서 세명의 팀원이 얻은 골드량을 매개변수로
받아, 팀의 평균 골드 획득량을 계산하는 함수 cal_average_gold를 정의하고 사
용해 보세요.
cal_average_gold(12000, 15000, 18000)
실행결과
15000.0
"""
print("=====Quiz 시작=====")

def cal_average_gold( *gold ):
  if gold == ():
    return 0
  else:
    total = 0
    for temp in gold:
      total += temp
    return float(total) / float(len(gold))

average_gold1 = cal_average_gold( 12000, 13000, 16000, 20000, 17000 )
average_gold2 = cal_average_gold()

print("실행결과")
print(average_gold1)
print(average_gold2)

print("=====Quiz 종료=====\n")
