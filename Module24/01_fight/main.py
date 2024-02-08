import random


class Warriors:
    def __init__(self, name, health=100):
        self.damage = 20
        self.name = name
        self.health = health

    def defence(self):
        self.health -= self.damage

    def attack(self):
        self.defence()



warrior_1 = Warriors('Эйрик', 100)
warrior_2 = Warriors('Бродди', 100)

while warrior_1.health > 0 and warrior_2.health > 0:
    hit = random.randint(1, 2)
    if hit == 1:
        print('{} наносит удар'.format(warrior_1.name))
        warrior_2.defence()
        print(f'Здоровье  {warrior_2.name}, {warrior_2.health}\n')
        if warrior_2.health <= 0:
            print(f'{warrior_1.name} одержал победу')

    if hit == 2:
        print('{} наносит удар'.format(warrior_2.name))
        warrior_1.defence()
        print(f'Здоровье  {warrior_1.name}, {warrior_1.health}\n')
        if warrior_1.health <= 0:
            print(f'{warrior_2.name} одержал победу')
