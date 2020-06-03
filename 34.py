def facto(num):
    counter = 1
    for i in range(2, num + 1):
        counter *= i
    return counter

def is_factorial(num):
    counter = 0
    stringed = str(num)
    for n in stringed:
        counter += facto(int(n))

    return num == counter

thirty_four = sum([i for i in range(3, 1000000) if (is_factorial(i))])
print(thirty_four) #40730