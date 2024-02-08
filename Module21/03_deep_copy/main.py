import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def find_key(struct, key, meaning):
    if key in struct:
        struct[key] = meaning
        return site
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, meaning)
            if result:
                return site



count_site = int(input('Сколько сайтов необходимо? '))
deep_copy = dict()
products = dict()
for _ in range(count_site):
    product_name = input('\nВведите название для нового продукта: ')
    key = {'title': f'Куплю/продам {product_name} телефон недорого','h2': f'У нас самая низкая цена на {product_name}'}
    for i in key:
        find_key(site, i, key[i])
    products_dict = f'Сайт для {product_name}'
    deep_copy = copy.deepcopy(site)
    products[products_dict] = deep_copy

    for key, value in products.items():
        print(key)
        print(value)

