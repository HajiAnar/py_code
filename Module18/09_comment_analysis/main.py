def count_uppercase_lowercase(text):
    uppercase = sum(1 for i in text if i.isupper())
    lowercase = sum(1 for i in text if i.islower())
    return uppercase, lowercase

# Пример использования:
text1 = input("Введите строку для анализа: ")
uppercase1, lowercase1 = count_uppercase_lowercase(text1)
print("Количество заглавных букв:", uppercase1)
print("Количество строчных букв:", lowercase1)
