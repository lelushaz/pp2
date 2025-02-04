import math
def is_prime(a):
    if a<2:
        return False
    else:
        for i in range(2,a):
           if (a%i) == 0:
                return False
        return True
    
numbers = [int(x) for x in input().split()]
primes = list(filter(lambda x: is_prime(x), numbers))
print(primes)