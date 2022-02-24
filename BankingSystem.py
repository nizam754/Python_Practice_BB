# Banking System:
bank_users = {'Alice': 1233, 'Samee': 25000, 'Robert': 30000}

print('Welcome to the bank.')
while True:
    print('What do you like to do?')
    print('  '+'1.VIEW BALANCE')
    print('  '+'2.VIEW ALL BANK INFO')
    print('  '+'3.UPDATE BALANCE')
    print('  '+'4.EXIT')

    desc = input()
    if desc == '1':
        print('Enter your Name, please: ')
        k = input()
        if k in bank_users.keys():
            print(k+' Your Bank balance is '+str(bank_users[k]))
        else:
            print('The user can not be found. Would you like to add the user to the account?')
            desc = input()
            if desc == 'YES':
                k = input('Enter your NAME please: ')
                v = input('Enter your BALANCE please: ')
                bank_users.update({k: v})

            else:
                print('Would like to exit?')
                desc = input()
                if desc == 'YES':
                    break

    elif desc == '2':
        for k, v in bank_users.items():
            print("USERNAME: "+str(k)+" BANK BALANCE: "+str(v))
    elif desc == '3':
        print('Enter your Name, please: ')
        k = input()
        if k in bank_users.keys():
            print('Do you want to add or subtract from your savings?')
            desc = input()
            if desc == 'ADD':
                temp_balance = bank_users[k]
                extra = input('Enter the amount you want to add: ')
                bank_users[k] = temp_balance+int(extra)
                print('Balance updated. It is: ')
                print(bank_users[k])
            elif desc == 'SUBTRACT':
                temp_balance = bank_users[k]
                extra = input('Enter the amount you want to subtract: ')
                bank_users[k] = temp_balance+int(extra)
                print('Balance update. It is: ')
                print(bank_users[k])
        else:
            print('There is no such account in the bank database.')

    elif desc == '4':
        break
