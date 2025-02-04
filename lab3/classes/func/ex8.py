def has007(num):
    n = []
    for x in num:
        if x == 0:
            n.append(x)
        elif x == 7:
                n.append(x)
    for i in range(len(n)-2):
        if n[i] == 0 and n[i+1] == 0 and n[i+2] == 7:
            return True
    return False
a= input()
num = [int(x) for x in a.split()]
print(has007(num))