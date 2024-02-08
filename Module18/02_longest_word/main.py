text = input('Введите текст: ').split()
text_list = [len(i) for i in text]
max_word = text[text_list.index(max(text_list))]

print('Самое длинное слово: {}'.format(max_word))
print('Длина этого слова: {}'.format(len(max_word)))
