import re
txt = "The rain in Spain abbbb"
x = re.findall(r'ab{2,3}', txt)
print(x)