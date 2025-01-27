import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_2165157.html").read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
count = 0
for tag in tags:
    num = int(tag.contents[0])
    count += num
print(count)
