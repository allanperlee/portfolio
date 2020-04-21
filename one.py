def multiples_of_3_5(n):
    counter = 0
    for i in range(3, n):
        if i % 3 == 0 or i % 5 == 0:
            counter += i

    return counter


print(multiples_of_3_5(1000))