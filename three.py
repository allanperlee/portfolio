#n = 600851475143

def is_prime(num):
    i = 2
    while i*i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def three(n):
    for i in range(100000, 1, -1):
        if is_prime(i) and n % i == 0:
            return i

print(three(600851475143))

#prints 6857