import re

phone_numbers = ['9999999999', '999999-999', '99999x9999']
phonenumbers_list = ['первый номер:', 'второй номер:', 'третий номер:']


for i_numbers,ph_numbers in enumerate(phone_numbers):

    if re.fullmatch(r'[89]\d{9}', ph_numbers):
        print(f'{phonenumbers_list[i_numbers]} номер: всё в порядке')

    else:
        print(f'{phonenumbers_list[i_numbers]} номер: не подходит')


