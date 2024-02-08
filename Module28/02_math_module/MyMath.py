import math
from abc import ABC


class MyMath(ABC):
    """Абстрактный класс MyMath"""

    @classmethod
    def circle_len(cls, radius: int) -> float:
        """Метод вычисления длины окружности"""
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        """Метод вычисления площади окружности"""
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, edge: int) -> float:
        """Метод вычисления объема куба"""
        return edge ** 3

    @classmethod
    def sphere_area(cls, radius: int) -> float:
        """Метод вычисления площади поверхности сферы"""
        return 4 * math.pi * radius ** 2
