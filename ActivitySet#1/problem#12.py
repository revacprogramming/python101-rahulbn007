# Regular Expressions
# https://www.py4e.com/lessons/regex
# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
hand=input('Enter the file name:')
handle=open(hand)
total=0
for line in handle:
     line=line.rstrip()
     ss=re.find