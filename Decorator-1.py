def outer(message):
    print('In the outer function')

    def inner():
        print('calling the inner function')
        print(message)

    return inner

# f = outer("Hello World")
# f()

def decorator(orginal_func):

    print('In the decorator function\n')

    def wrapper():
        print(f'wrapper executed before {orginal_func.__name__}()')

        if 10 > 5:
            print('yes it is true')

        return orginal_func() + ' extra string!'

    return wrapper
