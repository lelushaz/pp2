def histogram(list):
    for i in list:
        print('*' * i)
list=input()
list = [int(x) for x in list.split()]
histogram(list)