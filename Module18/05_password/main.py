while True:

    password = input('Придумайте пароль: ')
    length = len(password)
    capital_letters = len([letter for letter in password if letter.isupper()])
    numbers = len([letter for letter in password if letter.isdigit()])

    if (length >= 8) and (capital_letters >= 1) and (numbers >= 3):
        print('Это надежный пароль!')
        break

    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
