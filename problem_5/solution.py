# Lucas Soeth 2021-04-29
import numpy as np
found_primes = [2,3]

def is_prime(n):
    return all([n%i!=0 for i in range(2,n//2)])

def primes():
    for p in found_primes:
        yield p
    
    while True:
        p += 2
        if is_prime(p):
            found_primes.append(p)
            yield p

def prime_factors(num):
    factors = list()
    while (num != 1):
        for p in primes():
            if num%p==0:
                num /= p
                factors.append(p)
                break
    return factors

factors = list()

for i in range(2,21):
    f = prime_factors(i)
    for p in set(f):
        if (factors.count(p) < f.count(p)):
            for _ in range(factors.count(p) < f.count(p)):
                factors.append(p)


print(np.prod(factors))