def caesar_chiper(string, user_shift):
    char_list = [alphabet[(alphabet.index(sym) + user_shift) % 33] if sym != ' ' else ' ' for sym in string]
    new_str = ''
    for i in char_list:
        new_str += i
    return new_str


alphabet = 'абвгдеёжзийклмнопрстуфзцчшщъыьэюя'

input_str = input('Введите строку: ')
shift = int(input('Введите сдвиг: '))
output_str = caesar_chiper(input_str, shift)
print(output_str)
