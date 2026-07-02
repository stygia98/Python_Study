"""
Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
조건 : 모듈 파일명은 byme.py 로 작성
(모듈 사용 예제) 
import byme
byme.sign()
(출력 예제)
이 프로그램은 홍길동에 의해 만들어졌습니다. 
홈페이지 : http://hongGilDong.com/
이메일 : hongGilDong@gmail.com
"""

class Byme:
    # def byme(self):
    #     print("이 프로그램은 홍길동에 의해 만들어졌습니다.")
    #     print("홈페이지 : http://hongGilDong.com/")
    #     print("이메일 : hongGilDong@gmail.com")
    temp_name = "홍길동"
    temp_hpage = "http://hongGilDong.com/"
    temp_email = "hongGilDong@gmail.com"
    
    def byme(self, name=temp_name, hpage=temp_hpage, email=temp_email):
        print(f"이 프로그램은 {name}에 의해 만들어졌습니다.")
        print(f"홈페이지 : {hpage}")
        print(f"이메일 : {email}")
