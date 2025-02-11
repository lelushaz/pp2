
def gen_numbers(N):
    for i in range(1,N+1):
        if i%3==0 and i%4==0:
            yield i

N=int(input())
for i in gen_numbers(N):
    print(i,end=" ")
