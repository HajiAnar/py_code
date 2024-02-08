first_string = input('Введите первую строку: ')
second_string = input('Введите вторую строку: ')

if first_string == second_string:
    print('Строки идентичны')
elif len(second_string) != len(first_string):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига')
else:
    shift = 1

    for i in range(len(second_string) + 1):
        second_string = second_string[-1] + second_string[:-1]
        if second_string == first_string:

            print('Первая строка получается из второй со сдвигом', shift)
            break
        else:
            shift += 1

    if not shift:
       print('Первую строку нельзя получить из второй с помощью циклического сдвига')
