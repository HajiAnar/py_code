import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [(first_team[scores] if first_team[scores] > second_team[scores] else second_team[scores]) for scores in
           range(20)]

print('Первая команда:', first_team)
print('Вторая команда:', second_team)
print('Победители:', winners)
