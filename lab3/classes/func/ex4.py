def filter_prime(list):
    if list<2:
        return False
    else:
        for i in range(2,list):
           if (list%i) == 0:
                return False
        return True
numbers = [int(x) for x in input().split()]
primes = list(filter(lambda x: filter_prime(x), numbers))
print(primes)