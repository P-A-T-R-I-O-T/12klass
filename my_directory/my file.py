# Создать массив данных и сделать внутри этого массива поиск по Казани, России и  Миру
# Просмотреть внутри массива, сколько приходится на навыки.



import requests
import pprint


DOMAIN = 'https://api.hh.ru/'

url_vacancies = f'{DOMAIN}vacancies'


def search ():
    # Создал поиск по миру
    params_world = {
        'text': 'NAME:Python',
        # создал страницу т.к. данных много
        'page': 1
    }

    # Создал поиск по России
    params_russia = {
        'text': '(NAME:Python) AND russia',
        # создал страницу т.к. данных много
        'page': 1
    }


    # Создал поиск по Казани
    params_kazan = {
        'text': '(NAME:Python) AND kazan',
        # создал страницу т.к. данных много
        'page': 1
    }

    params = {
        'text': 'NAME: (Python) AND kazan',
        # страница
        'page': 1
    }

params= {
        'text': 'NAME:Python',
        # создал страницу т.к. данных много
        'page': 1
    }
result = requests.get(url_vacancies, params=params).json()

# print(result.status_code)
# pprint.pprint(result.json())

items = result['items']

#first = items[0]

pprint.pprint(items)
# Нужно осуществить сортировку по 'area':('name': ''Казань'')
'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}