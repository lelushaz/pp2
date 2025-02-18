import re
txt = "The rain in Spain"
x = re.findall(r'ab*', txt)
print(x)