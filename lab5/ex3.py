import re
txt = "The rain in Spain abbb asdda_asdasd_asdsad a_a a_b"
x=re.findall(r'\b[a-z]+_[a-z]+\b', txt)
print(x)