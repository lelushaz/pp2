import re
txt="python_regex"
x=re.sub(r'_([a-z])', lambda x: x.group(1).upper(),txt)
x=re.sub(r'\b([a-z])', lambda x: x.group(1).upper(),x)
print(x)