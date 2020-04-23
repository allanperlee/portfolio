def is_thirty(n):
    o = sum([int(x)**5 for x in str(n)])
    if o == n:
        return True

counter = 0
for i in range(2, 2000000):
    if is_thirty(i):
        counter += i

print(counter)

#prints 443839
