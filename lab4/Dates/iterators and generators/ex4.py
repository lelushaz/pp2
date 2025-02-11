def gen_squares(a,b):
    for i in range(a,b):
        yield i**2
a=int(input())
b=int(input())
for i in gen_squares(a,b):
    print(i,end=" ")
for i in range(a,b):
    print(i**2)