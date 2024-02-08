class NotNameError(Exception):
    pass

class NotEmailError(Exception):
    pass

file_out_good = 'registrations_good.log'
file_out_bad = 'registrations_bad.log'

def check_exceptions():
    if not (str(name)).isalpha():
        raise NotNameError('Неверное имя')
    elif mail.find('@') == -1 or mail.find('.') == -1:
        raise NotEmailError('Невереный Email')
    elif not 10 <= int(age) <= 99:
        raise ValueError('Неверный интервал возвраста')
    elif not age[:-2].isdigit():
        raise ValueError('Возраст - не число')
    with open(file_out_good, mode='a', encoding='utf-8') as file_good:
        file_good.write(line)


with open('registrations.txt', 'r', encoding='utf-8') as registr_file:
    for line in registr_file:
        try:
            name, mail, age = line.split(' ')
            check_exceptions()
        except (ValueError, NotNameError, NotEmailError) as exc:
            with open(file_out_bad, mode='a', encoding='utf-8') as file_bad:
                file_bad.write(f'{line}! Вид ошибки {exc}')

