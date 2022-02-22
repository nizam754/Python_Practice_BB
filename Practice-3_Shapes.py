def area_func():
    print('Enter the shape to find the area: ')
    shape = input()

    if shape == 'CIRCLE':
        print('PLEASE ENTER THE RADIUS: ')
        r = float(input())
        area = 3.1416*r*r
        print('The area is: ')
        print(area)
    elif shape == 'TRIANGLE':
        print('PLEASE ENTER THE BASE: ')
        base =float(input())
        print('PLEASE ENTER HEIGHT: ')
        height = float(input())
        area = 0.5*base*height
        print('The area is: ')
        print(area)
    elif shape == 'RECTANGLE':
        print('PLEASE ENTER THE LENGTH: ')
        length = float(input())
        print('PLEASE ENTER THE WIDTH: ')
        breadth = float(input())
        area = length*breadth
        print('The area is: ')
        print(area)
    elif shape == 'SQUARE':
        print('PLEASE ENTER THE LENGTH: ')
        length = float(input())
        area = length**2
        print('The area is: ')
        print(area)
    elif shape == 'TRAPEZIUM':
        print('PLEASE ENTER THE SIDE 1: ')
        side1 = float(input())
        print('PLEASE ENTER THE SIDE 2: ')
        side2 = float(input())
        print('PLEASE ENTER THE height: ')
        height = float(input())
        area = 0.5*(side1+side2)*height
        print('The area is: ')
        print(area)

area_func()
