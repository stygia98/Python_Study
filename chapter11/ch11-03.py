# https://pypi.org/project/beautifulsoup4/

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

print(soup.find(string="bad"))

if soup.find(string="bad"):
    print("검색됨")
else :
    print("검색안됨")

print(soup.i)
