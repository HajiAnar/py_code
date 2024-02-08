line = input('Введите строку: ')

reversed = line[line.find('h') + 1:line.rfind('h')]
new_list = reversed[::-1]
print('Развёрнутая последовательность между первым и последним h:', new_list)
