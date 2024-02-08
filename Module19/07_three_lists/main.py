array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print('Задача 1.\nРешение с множествами:')
print(*set(array_1).intersection(set(array_2), set(array_3)))

print('\nЗадача 1.\nРешение без множеств:')
main_list_1 = []
for i in array_1:
    if i in (array_2 and array_3):
        main_list_1.append(i)

print(*main_list_1)

print('\nЗадача 2.\nРешение с множествами:')
print(*list(set(array_1) - set(array_2 + array_3)))

print('\nЗадача 2.\nРешение без множеств:')
main_list_2 = []
for i in array_1:
    if i not in (array_2 or array_3):
        main_list_2.append(i)

print(*main_list_2)