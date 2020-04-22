def twenty(n):
    one = 1
    for i in range(1, n+1):
        one *= i
    final = sum([int(j) for j in str(one)]) 
    return final


print(twenty(100))

#prints 648