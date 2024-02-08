import random

original_list = [random.randint(0, 10) for _ in range(10)]
print(f"Оригинальный список: {original_list}")

#вариант 1
zip_list = zip(original_list[::2], original_list[1::2])
new_list = []
for pair in zip_list:
    new_list.append(pair)
print(f'Новый список, {new_list}')



#вариант2
new_list = [(original_list[i], original_list[i + 1]) for i, j in enumerate(original_list) if i % 2 == 0 ]
print(f'Новый список, {new_list}')

