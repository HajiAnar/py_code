import re

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

result_private_auto = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', text)
print('Список номеров частных автомобилей',result_private_auto)


result_taxi_auto = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b', text)
print('Список номеров автомобилей такси', result_taxi_auto)

