from re import findall as fa
import re
import sys

with open('BookOfMormonProcessed.csv') as f:
  s = f.readlines()

matchVerses = []

for verse in s:
  matches = fa('(?:\w+,? ){,7}command(?:ment)?s?(?:,? \w+){,7}',verse, re.IGNORECASE)
  
  for i in matches:
    if fa(r'\bprosper\b|\bbless\b|\bpromise\b',verse, re.IGNORECASE):
#    if fa(r'\bif\b',i, re.IGNORECASE) and fa(r'(?:\bkeep\b)|(?:\bobey\b)|(?:\bobedient\b)|(?:\bprosper\b)',i, re.IGNORECASE):
      print i
      matchVerses.append(verse)
      break

for i,j in enumerate(matchVerses):
  print i,j

print "Matches found:",len(matchVerses)
