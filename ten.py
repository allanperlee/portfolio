def is_prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def ten(num):
    counter = 0
    for i in range(2, num + 1):
        if is_prime(i):
            counter += i
    return counter

print(ten(2000000))

#took longer than expected, may have to revisit this algorithm, still got
#the correct answer: 142913828922