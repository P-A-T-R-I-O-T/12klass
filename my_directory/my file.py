import requests
import pprint


DOMAIN = 'https://api.hh.ru/'

url_vacancies = f'{DOMAIN}vacancies'

params = {
    'text': 'Python',
    # есть страницы т.к. данных много
    'page': 1
}

result = requests.get(url_vacancies, params=params).json()
#print(result.status_code)
#pprint.pprint(result.json())

items = result['items']

first = items[0]

pprint.pprint(first)