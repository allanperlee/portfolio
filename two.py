def two(maximum):
    a, b = 0, 1
    while a < maximum:
        yield a
        a, b = b, a+b

final = sum([x for x in two(4000000) if x % 2 == 0])
print(final)

# prints 4613732