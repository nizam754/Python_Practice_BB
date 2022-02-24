# This program simulates a phone-book

contact_no = {'Sam': 0000, 'Smith': 1111, 'Ron': 9898}
x = 0

while x < 5:
    print('Enter your Name(press ENTER to exit): ')
    name = input()

    if name == '':
        break

    if name in contact_no:
        print('The contact number of '+name +' is ' +str(contact_no[name]))
    else:
        print("There is no such name in the phone-book. Do you want to add it?")
        desc = input()

        if desc == 'yes':
            print('Enter the number: ')
            num = input()
            contact_no[name] = num
            print('Dictionary Updated.')
        elif desc == 'no':
            print('Do you want to quit?')
            desc = input()
            if desc == 'yes':
                break
            else:
                print('Keep searching.')

    x = x+1
