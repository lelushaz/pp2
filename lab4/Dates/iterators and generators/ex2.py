def gen_even_numbers(N):
    for i in range(1,N+1):
        if i%2==0:
            yield i

N=int(input())
for i in gen_even_numbers(N):
    print(i,end=", ")