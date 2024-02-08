def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
        return sym_dict

text = input('Введите текст: ')
hist = histogram(text)
text_dict = dict()
print('Оригинальный словарь частот\n')
for i_sym in sorted(hist.keys()):
  print(i_sym, ':', hist[i_sym])

print('Инвертированный словарь частот\n')
for i_letter, i_num  in hist.items():
  text_dict.setdefault(i_num, []).append(i_letter)
for i in text_dict:
  print(i, ':', text_dict[i])

