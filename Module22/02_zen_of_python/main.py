zen_file = open('zen.txt', 'r', encoding='utf-8')

reverse_zen = zen_file.readlines()

reverse_zen.reverse()

print(''.join(reverse_zen))

zen_file.close()
