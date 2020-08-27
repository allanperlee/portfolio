def is_abundant (integer):
    final = 0
    for i in range(1, integer):
        if integer % i == 0:
            final += i
    return final > integer

sum_of_two_abundants = [False] * 28124
limit = 28123
the_abundants = [i for i in range(0, limit + 1) if is_abundant(i)]
counter = 0

for i in the_abundants:
    for j in the_abundants:
        if i + j <= limit:
            sum_of_two_abundants[i + j] = True


for k in range(0, len(sum_of_two_abundants)):
    if sum_of_two_abundants[k] == False:
        counter += k

print(counter)
#prints 4179871


