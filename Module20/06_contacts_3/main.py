phone_dict = dict()

def add_contacts(dict_):
    name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
    if name not in phone_dict:
        phone_number = int(input('Введите номер телефона: '))
        phone_dict[name] = phone_number
        print(phone_dict)
    else:
        print('Это имя уже есть в списке')


def search_contact(dict_):
    search = input('Введите фамилию для поиска: ')
    for person in phone_dict:
        if search.lower() == person[0].lower():
            print(person[0], person[1], phone_dict[person])
        else:
            print('Такого человека в контактах нет ')



while True:
    command = int(input('1. Добавить контакт\n'
                        '2. Найти контакт\n'
                        'Введите номер действия: '))
    print()
    if command == 1:
        add_contacts(phone_dict)
    else:
        search_contact(phone_dict)

