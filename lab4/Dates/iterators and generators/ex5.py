def gen_returns(N):
    while N>=0:
        yield N
        N-=1
N=int(input())
for i in gen_returns(N):
    print(i)