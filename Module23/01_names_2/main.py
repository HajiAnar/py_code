line_count = 0
sym_result = 0

with open('people.txt', 'r', encoding='utf-8') as peoples:
    try:
        for line in peoples:
            try:
                len_line = len(line)
                line_count += 1
                if line.endswith('\n'):
                    len_line -= 1
                sym_result += len_line
                if len_line < 3:
                    raise ValueError
            except ValueError:
                print('Имя в строке {} меньше трех букв'.format(line_count))
                with open('errors.log', 'a') as error_file:
                    error_file.write(line)

    except FileNotFoundError:
        print('Файл не найден ')

    finally:
        print('Сумма символов: ', sym_result)
