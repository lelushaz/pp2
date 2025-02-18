import re
txt = "The rain in Spain spab baaaaaadsb abbb asdda_asdasd_asdsad a_a a_b ab a_b aaaaaaaaab bab 12ab ; ,"
x = re.sub("\s|,|;", ":", txt)
print(x)