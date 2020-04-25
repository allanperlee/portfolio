products = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if i*j == int(str(i*j)[::-1]):
            products.append(i*j)
    

print(max(products))
#prints 906609
