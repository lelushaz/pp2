import re
txt = "The rain in Spain abbb"
x = re.search(r'a(b{2,3})', txt)
print(x)