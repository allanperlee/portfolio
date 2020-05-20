prime = lambda n: all(n % i != 0 for i in range(2, n//2+1))

def seven(num):
    counter = 0
    primes = 1
    #counter only increases when a prime number is found
    while counter < num:
        #every round iterates the primes variable starting at 2 until num prime is found
        primes += 1
        if prime(primes):
            counter += 1
    return primes
    #prime is found when the counter is not less than num
    
print(seven(10001))

#prints 104743