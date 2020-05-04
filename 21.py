def is_amicable(num):
    total = sum([i for i in range(1, num) if num % i == 0])
    if total == num:
        return False
    total_1 = sum([j for j in range(1, total) if total % j == 0])
    return total_1 == num


twenty_one = sum([i for i in range(1, 10000) if is_amicable(i)])
print(twenty_one)

#prints 31,626