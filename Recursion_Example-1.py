# sum using recursion:

# sum using loop/ iteration:

def sum_f(n):
    sum = 0

    for i in range(1, n+1):
        sum = sum+i

    return sum

print(sum_f(4))

def sum_f2(n):
    if n == 0:
        return 0

    return n+sum_f2(n-1)

print(sum_f2(4))
