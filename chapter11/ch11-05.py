# 내장함수

# import glob
# print(glob.glob(".\chapter11\*.py"))

import os
# print(os.getcwd())
# print(os.listdir())


# if os.path.exists("sample_text"):
#     print("파일 있음 >>> 파일을 삭제합니다")
#     os.rmdir("sample_text")
# else :
#     print("파일 없음 >>> 파일을 생성합니다")
#     os.mkdir("sample_text")


import time
print(time.localtime())
print(time.strftime("%Y-%m-%d - %H:%M:%S"))

import datetime
today = datetime.date.today()
print("Today : ", today)

td = datetime.timedelta(days=100)
print("+100 days : ", today + td)
