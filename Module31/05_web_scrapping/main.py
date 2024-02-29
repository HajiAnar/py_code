import requests
import re


url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url).text

items = re.findall(r'<h3.*>(.+)</h3>', response)
print(items)



# В данном случае запрос request.get заменен на загрузку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()

