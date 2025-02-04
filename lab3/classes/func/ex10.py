def uniq(x):
    only_uniq = []
    for i in x:
        if i not in only_uniq:
            only_uniq.append(i)
    print(only_uniq)
inpt = input()
x = inpt.split()
uniq(x)