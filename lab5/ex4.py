import re
txt = "The rain in Spain abbb asdda_asdasd_asdsad a_a a_b"
x=re.findall(r'[A-Z][a-z]+', txt)
print(x)