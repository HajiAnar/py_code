class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)

"""Класс Mydict дочерний класс от dict.
    Arg:
    key - ключ словаря
    default - значение в словаре не найдено
    Метод-геттер: возвращает ключ значения, если оно найдено в словаре, возвращает 0, если значение в словаре не найдено  """

new_dict = MyDict()
new_dict['aaa'] = 1
new_dict['bbb'] = 2
new_dict['ccc'] = 3
print(new_dict)

print(new_dict.get('bbb'))
print(new_dict.get('420'))
