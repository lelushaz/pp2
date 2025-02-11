def squares(N):
    for i in range(1,N): 
        yield i**2
N=int(input())
print(*squares(N))