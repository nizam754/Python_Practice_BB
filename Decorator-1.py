def outer(message):
    print('In the outer function')

    def inner():
        print('calling the inner function')
        print(message)

    return inner

f = outer("Hello World")
f()
