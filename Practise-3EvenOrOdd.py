import math
# a Function to check a no is odd or even

def check_even_odd(n):
    if n%2 == 0:
        print('The number is even')
    else:
        print('The number is odd')

def check_prime(n):
    count = 0
    for i in range(2, math.floor(math.sqrt(n))+1):

        if n % i == 0:
            print('The number is not prime')
            break
        count = count+1
    if count+2 == math.floor(math.sqrt(n))+1:
        print('The number is prime ')
        
n = int(input())
check_even_odd(n)
check_prime(n)
