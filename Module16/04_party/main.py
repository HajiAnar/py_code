guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

command = ' '

while command != 'пора спать':
    print(f'\nСейчас на вечеринке {len(guests)} гостей {guests} ')
    command = input('Гость пришел или ушел? ')
    if command == 'пришел' and len(guests) < 6:
        name = input('Имя гостя: ')
        print('Привет,', name)
        guests.append(name)
    elif command == 'пришел':
        name = input('Имя гостя: ')
        print('Прости,', name, 'мест нет')
    elif command == 'ушел':
        name = input('Имя гостя: ')
        if name in guests:
           print('Пока, ', name)
           guests.remove(name)
        else:
            print('Такого имени нет в списке')
print('Вечеринка закончилась, все легли спать')

