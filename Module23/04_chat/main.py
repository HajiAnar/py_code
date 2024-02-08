import time
user_name = input('Введите имя пользователя: ')

while True:
    print('1: увидеть сообщения чата\n'
          '2: написать сообщение')
    answer = input('Ваш выбор: ')
    if answer == '1':
        try:
            with open('chat_history.txt', 'r') as chat_file:
                messages = chat_file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('Пока сообщений нет\n')

    elif answer == '2':
        user_message = input('Введите сообщение: ')
        with open('chat_history.txt', 'a') as chat_file:
            chat_file.write('{name}: {message}\n'.format(
                name=user_name, message=user_message))
    else:
        print('Такой команды нет. Введите 1 или 2.')


