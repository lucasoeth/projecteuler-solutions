# Lucas Soeth 2021-04-29
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

num = 600851475143
prime_factors = list()
while (num != 1):
    for p in primes():
        if num%p==0:
            num /= p
            prime_factors.append(p)
            break

print(max(prime_factors))