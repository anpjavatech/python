import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2165159.xml'

uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
total = 0
for result in counts:
    total += int(result.text)

print('Sum:', total)
