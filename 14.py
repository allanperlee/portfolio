def collatz(num, counter = 1):
    while num > 1:
        counter += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num  = 3 * num + 1
    return counter

collatzes = [collatz(i) for i in range(1, 1000000)]
final = collatzes.index(525)
print(final)

#prints 837798