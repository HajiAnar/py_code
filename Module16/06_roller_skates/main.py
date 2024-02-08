count_skates = int(input('Количество коньков в прокате: '))
skates_list = []
size_list = []
count = 0

for i in range(count_skates):
    skates = int(input(f'Размер {i + 1} пары: '))
    skates_list.append(skates)

people = int(input('Количество человек: '))
for i in range(people):
    size = int(input(f'Введите размер {i+1}-го человека '))
    size_list.append(size)

for size in size_list:
    for j in range(len(skates_list)):
        if skates_list[j] >= size:
            skates_list.remove(skates_list[j])
            count += 1
            break

print('Наибольшее кол-во людей, которые могут взять ролики:', count)
