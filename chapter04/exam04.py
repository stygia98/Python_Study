"""
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com 
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver 
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성 (nav) (5) 
(1) (!)
예) 생성된 비밀번호 : nav51!
"""



"""
exam = "http://naver.com"

print(f"예) {exam}")
print("=============================")
findIndex1 = exam.find("/")
findIndex2 = exam.find(".", findIndex1)
print(f"처음 세자리 : {exam[findIndex1+2:findIndex1+5]}")

length1 = len(exam[findIndex1+2:findIndex2])
print(f"글자갯수 : {length1}")

count1 = exam.count("e")
print(f"'e'개수 : {count1}")

print("=============================")
pw = exam[findIndex1+2:findIndex1+5] + str(length1) + str(count1) + "!"
print(f"생성된 비밀번호 : {pw}")
"""



# url = input("사이트를 입력하면 암호를 생성 >> ")
url1 = "http://naver.com"
url2 = url1.replace("http://", "")
print(url2)

find = url2.find(".")
print(find)

url3 = url2[:find]
print(url3)

url4 = url3[:3]
print(url4)

password = url4 + str(len(url3)) + str(url3.count("e")) + "!"
print(f"생성된 비밀번호 : {password}")
