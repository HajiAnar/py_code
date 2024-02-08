class Water:
    name = 'Вода'
    def __str__(self):
        return 'Вода'
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None
class Fire:
    name = 'Огонь'
    def __str__(self):
        return 'Огонь'
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        else:
            return  None

class Earth:
    name = 'Земля'
    def __str__(self):
        return 'Земля'
    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None

class Air:
    name = 'Воздух'
    def __str__(self):
        return 'Воздух'
    def __add__(self, other):
        if isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        else:
            return None

class Dust:
    name = 'Пыль'
    def __str__(self):
        return 'Пыль'

class Lava:
    name = 'Лава'
    def __str__(self):
        return 'Лава'

class Storm:
    name = 'Шторм'
    def __str__(self):
        return 'Шторм'
class Dirt:
    name = 'Грязь'
    def __str__(self):
        return 'Грязь'
class Steam:
    name = 'Пар'
    def __str__(self):
        return 'Пар'
class Lightning:
    name = 'Молния'
    def __str__(self):
        return 'Молния'

class Stone:
    name = 'Камень'
    def __str__(self):
        return 'Камень'

w = Water()
f = Fire()
a = Air()
e = Earth()
s = Stone()

new_elem = w + f
print(f'Смешиваем {w.name} и {f.name} и получаем {new_elem}')

new_elem2 = a + e
print(f'Смешиваем {a.name} и {e.name} и получаем {new_elem2}')

new_elem3 = a + s
print(f'Смешиваем {a.name} и {s.name} и получаем {new_elem3}')
