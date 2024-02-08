import re

s = input('Введите строку: ')
print(re.sub(r'(.)\1*', lambda x: f'{x.group(1)}{len(x.group())}', s))

