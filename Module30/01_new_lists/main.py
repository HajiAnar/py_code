from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
new_floats:List[float] = list(map(lambda num: round(num ** 3, 3), floats))
print(new_floats)


new_float:List[float] = [round(num ** 3, 3) for num in floats]
print(new_float)


names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
new_names: List[str] = list(filter(lambda name: len(name) >= 5, names))
print(new_names)

new_names2: List[str] = [name for name in names if len(name) >= 5]
print(new_names2)


numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
numbers1 = reduce(lambda previous, elem: previous * elem, numbers)
print(numbers1)