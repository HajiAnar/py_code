class Property:

    tax_rate = 0
    def __init__(self, worth):
        self.__worth = worth

    """ Property -родительский класс
        tax_rate(int)- ставка налога
        worth(int) -стоимость имущества"""

    def get_worth(self):
        return self.__worth
    """Геттер для получения стоимости"""

    def set_worth(self, worth=None):
        self.__worth = worth
    """Сеттер для установления стоимости"""

    def get_tax(self):
        return round(self.__worth / self.tax_rate, 2)
    """Геттер для получения налога на имущество"""

    def __str__(self):
        return   f'Налог на  имущество {self.get_tax()}'
    """Метод вывода информации о налоге на экран"""


class Apartment(Property):
    tax_rate = 1000
    def __init__(self, worth):
        super().__init__(worth)
    """Класс Apartment (квартира)
    tax_rate = 1000"""

class Car(Property):
    tax_rate = 200

    def __init__(self, worth):
        super().__init__(worth)

    """Класс Car (автомобиль)
        tax_rate = 200"""
class CountryHouse(Property):

    tax_rate = 1500

    def __init__(self, worth):
        super().__init__(worth)

    """Класс CountryHouse (загородный дом)
            tax_rate = 1500"""


print('Расчет налогов')
bank_account = int(input('Cколько денег на счете? '))
apartment_worth = int(input('Стоимость квартиры: '))
apart_tax = Apartment(apartment_worth)
print(apart_tax)

car_worth = int(input('Стоимость автомобиля: '))
car_tax = Car(car_worth)
print(car_tax)

country_house_worth = int(input('Стоимость загородного дома: '))
country_tax = CountryHouse(country_house_worth)
print(country_tax)


sum_tax = apart_tax.get_tax() + car_tax.get_tax() + country_tax.get_tax()
print('Сумма налогов', sum_tax)
if sum_tax > bank_account:
    print('Денежных средств недостаточно для покрытия налогов', abs(sum_tax - bank_account))
else:
    print('Собственных средств достаточно на покрытие налогов')
