password = 'A1B2C3'

not_matched = True

while not_matched:
    given_password = input('Enter Your Password: ')

    if given_password != password:
        print('Invalid Password. Try Again')
        
    else:
        print('Password Matched')
        not_matched = False
