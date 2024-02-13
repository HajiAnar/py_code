
def count_unique_characters(message):
    message = message.lower()
    return sum(map(lambda c: message.count(c) == 1, set(message)))


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
