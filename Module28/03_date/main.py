class Date:
    """Класс Date
    Атрибуты:
    day - день: int
    month - месяц: int
    year - год: int"""
    def __init__(self, day: int = 0, month=0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        """Метод вывода информации на экран"""
        return f'День: {self.day}\tМесяц: {self.month}\tГод: {self.year}'

    @classmethod
    def _split_date(cls, date: str) -> None:
        """Метод разбивки даты на day, month, year"""
        date_list = []
        if '-' in date:
            date_list = date.split('-')
        elif '/' in date:
            date_list = date.split('/')
        elif '.' in date:
            date_list = date.split('.')
        if len(date_list) != 3:
            cls.day = None
            cls.month = None
            cls.year = None
        else:
            cls.day, cls.month, cls.year = map(int, date_list)

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        """Метод проверки корректности даты"""
        cls._split_date(date)
        return 0 < cls.day <= 31 and 0 < cls.month <= 12 and 0 < cls.year <= 9999

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        """Метод конвертации"""
        cls._split_date(date)
        date_obj = cls(cls.day, cls.month, cls.year)
        return date_obj


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

