def main():
    cards_count = int(input('Количество видеокарт: '))
    old_list = get_cards_list(cards_count)
    print(f'Старый список видеокарт: {old_list}')
    new_list = delete_old_card(old_list)
    print(f'Новый список видеокарт: {new_list}')

def get_cards_list(count):
    cards_list = []
    for i in range(1, count + 1):
        card = int(input(f'{i} Видеокарта: '))
        cards_list.append(card)
    return cards_list

def delete_old_card(cards_list):
    oldest_card = max(cards_list)
    list_without_old = []
    for card in cards_list:
        if card != oldest_card:
            list_without_old.append(card)
    return list_without_old

main()