first_list = [1, 5, 3]
second_list = [1, 5, 1, 5]
third_list = [1, 3, 1, 5, 3, 3]

first_list.extend(second_list)
elem_five = 0
for i in first_list:
    if i == 5:
        elem_five += 1
        first_list.remove(i)
print('Кол-во цифр 5 при первом объединении: ', elem_five)


first_list.extend(third_list)
elem_three = 0
for i in first_list:
    if i == 3:
        elem_three += 1
print('Кол-во цифр 3 при втором объединении: ', elem_three)
print('Итоговый список: ', first_list)
