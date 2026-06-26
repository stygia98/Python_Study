"""
Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다. 보고서
는 항상 아래와 같은 형태로 출력되어야 합니다.
- X 주차 주간보고
- 부서 :
- 이름 :
- 업무 요약 :
1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다
"""
print("=====Quiz 시작=====")

# with open(txt_title, "r", encoding="UTF-8") as txt_handle:
#   txt_handle.write()

for i in range(1, 11):
  txt_title = str(i)+"주차.txt"
  print(txt_title)
  txt_handle = open("./"+txt_title, "w", encoding="UTF-8")
  txt_handle.write(f"- {i} 주차 주간보고\n")
  txt_handle.write(f"- 부서 : 프로그래밍부\n")
  txt_handle.write(f"- 이름 : 홍길동\n")
  txt_handle.write(f"- 업무 요약 : 위클리 프로그래밍 {i}\n")
  txt_handle.close()

print("=====Quiz 종료=====\n")
