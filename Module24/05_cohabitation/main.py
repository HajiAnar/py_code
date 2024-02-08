import random

class Home:
    def __init__(self):
        self.food = 50
        self.money = 0

class Person:
    def __init__(self, name, home):
        self.name = name
        self.fullness = 50
        self.home = home

    def to_eat(self):
        self.home.food -= 10
        self.fullness += 10
        print(f'{self.name} поел.\n'
              f'Сытость = {self.fullness}\n'
              f'В доме осталось {self.home.food} еды')

    def is_alive(self):
        return self.fullness > 0

    def to_work(self):
        self.fullness -= 10
        self.home.money += 10
        print(f'{self.name} поработал.\n'
              f'Сытость = {self.fullness}\n'
              f'В доме  {self.home.money} денег')

    def to_play(self):
        self.fullness -= 10
        print(f'{self.name} поиграл.\n'
              f'Сытость = {self.fullness}')

    def go_shop(self):
        self.home.food += 10
        self.home.money -= 10
        print(f'{self.name} сходил в магазин.\n'
              f'Продуктов в доме = {self.home.food}\n'
              f'В доме  {self.home.money} денег')

def one_day(person):
    cubes_number = random.randint(1, 6)
    if person.fullness < 0:
        print(f'К сожалению, {person.name} умер ')
        return 1
    if person.fullness < 20:
        person.to_eat()
    elif person.home.food < 10:
        person.go_shop()
    elif person.home.money < 50:
        person.to_work()
    elif cubes_number == 1:
        person.to_work()
    elif cubes_number == 2:
        person.to_eat()
    else:
        person.to_play()


def life():
   apartment = Home()
   residents = [Person('Vasya', apartment), Person('Masha', apartment)]
   day = 0
   while len(residents) > 0 and day < 366:
       day += 1
       for person in residents:
           one_day(person)
           if not person.is_alive():
               print(f'К сожалению, ваш {person.name} персонаж не пережил {day} день')
               residents.remove(person)

   print(f'Персонажи прожили {day} дней')

life()
