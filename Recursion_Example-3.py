# Recursive fibonacci

def fibo_recursive(n):
    if n <= 1:
        return n
    return fibo_recursive(n-1)+fibo_recursive(n-2)

print(fibo_recursive(6))
