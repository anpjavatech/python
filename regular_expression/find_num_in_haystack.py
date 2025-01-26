import re

fileHandle = open('./fixtures/actual.txt', 'r')
total = 0
for line in fileHandle:
   numList = re.findall('([0-9]+)', line)
   if len(numList) <= 0: continue
   print(numList)
   for num in numList:
      total += int(num)

print(total)