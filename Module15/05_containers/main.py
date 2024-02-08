
list_tov = []
all_tov = int(input('Количество контейнеров: '))
for _ in range(all_tov):
    kg_tov = int(input('Введите вес контейнера: '))
    list_tov.append(kg_tov)
new_tov = int(input('Новый контейнер: '))
sort = 0
while sort < len(list_tov) and list_tov[sort] >= new_tov:
    sort += 1
print('Номер, который получит новый контейнер:', sort + 1)

