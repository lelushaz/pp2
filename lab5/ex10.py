import re
txt = "PythonRegex"
x = re.sub(r'([a-z])([A-Z])', r'\1_\2', txt)
print(x.lower())