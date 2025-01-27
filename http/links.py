import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter the url : ")
counts = int(input("Enter the count : "))
position = int(input("Enter the position : "))

result = None
for count in range(counts):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    url = tags[position-1].get('href', None)

    name = url.split('_')[2].split('.html')[0]
    result = name

print(result)
