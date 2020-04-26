prime = lambda n: all(n % i != 0 for i in range(2, n//2+1))

def seven(num):
    counter = 0
    primes = 1
    while counter < num:
        primes += 1
        if prime(primes):
            counter += 1
    return primes
    
print(seven(10001))