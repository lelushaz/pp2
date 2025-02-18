import re
txt="pythonAegexAweqweqwe"
a = re.findall('[A-Z][^A-Z]*', txt)
x=a
print(x)