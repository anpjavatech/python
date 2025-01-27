import json
import urllib.request, urllib.parse, urllib.error

url = input("Enter the location: ")
res = urllib.request.urlopen(url).read()
info = json.loads(res)
comments = info["comments"]

total = 0
for comment in comments:
    count = int(comment["count"])
    total += count

print('Sum:', total)

