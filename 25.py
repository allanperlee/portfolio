sequence = [1, 1]
start = 2
limit = 10**999

while start < 10000:
    fibonacci = sequence[start - 1] + sequence[start - 2]
    if fibonacci > limit:
        break
    sequence.append(fibonacci)
    start += 1

print(start + 1)
#prints 4782