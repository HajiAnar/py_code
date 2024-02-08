import os
from typing import TextIO


class File:
    """Класс File
    Атрибуты:
    filename - имя файла: str
    mode - режим: str"""
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> TextIO:
        """Менеджер контекста"""
        if os.path.isfile(self.filename):
            self.file = open(self.filename, self.mode, encoding='utf8')
        else:
            self.file = open(self.filename, 'w+')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """Метод финализации контекста"""
        self.file.close()

        if exc_type and issubclass(exc_type, IOError):
            return True



with File('example.txt', 'r') as file:
    file.write('Всем привет!')
