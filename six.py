def sum_square(n):
    one = 0
    two = 0
    for i in range(0, n+1):
        one += (i**2)
        two += i
    
    two_squared = two **2
    final = two_squared - one

    return final

print(sum_square(100))