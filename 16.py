def sixteen(num, exp):
    product = num**exp
    final = sum([int(i) for i in str(product)])
    return final

print(sixteen(2, 1000))