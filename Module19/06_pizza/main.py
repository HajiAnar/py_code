order_dict = dict()

for i in range(0, int(input('Введите количество заказов: '))):
    order = input(f'{i+1}-й заказ: ').split()
    if order[0] in order_dict:
        if order[1] in order_dict[order[0]]:
            order_dict[order[0]][order[1]] += int(order[2])
        else:
            order_dict[order[0]][order[1]] = order[2]
    else:
        order_dict[order[0]] = dict({order[1]:int(order[2])})

for i in sorted(order_dict):
    print(f'\n {i} :')
    for j in sorted(order_dict[i]):
        print(f'\t {j} : {order_dict[i][j]}')
