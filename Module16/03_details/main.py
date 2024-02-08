shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail_name = input('Какую деталь искать? ')
count = 0
total_summ = 0

for detail in shop:
        if detail[0] == detail_name:
                count += 1
                price = detail[1]
                total_summ += price

print('Количество деталей: ', count)
print('Общая стоимость: ', total_summ)

