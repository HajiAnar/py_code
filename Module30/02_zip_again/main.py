from typing import List



letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

result = map(lambda letter, num: (letter, num), letters, numbers)
print(list(result))
