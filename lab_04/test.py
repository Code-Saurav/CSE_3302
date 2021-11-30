import re

txt = "The rain in Spain"

x = re.search('""',txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

print(x)