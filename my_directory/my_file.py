import requests
import pprint
from parser_hh import skills

# Поиск внутри hh
DOMAIN = 'https://api.hh.ru/'
url_vacancies = f'{DOMAIN}vacancies'
search_r = 113  # Поиск в нутри России
search_m = 1  # Поиск по Москве
earch_k = 1624 # Поиск по Казани
skils_list = skills
found_list = []
procent_sum = []
general_list = []


def hh_api(result_list_final, area = search_r): # Поиск по hh
        params = {
                'text': 'NAME: python OR DESCRIPTION:' f'{result_list_final}', # Поиск по названию вакансии и внутреннем страничкам из этой списка вакансий
                'area': area, # Место поиска
                'page': 1 # создал страницу т.к. данных много
        }
        result = requests.get(url_vacancies, params=params).json()
        found = result['found']# запрос на количество вакансий по каждому скилу
        found_list.append(found) # Сумирует общую количесво найденых страниц, по каждому skil




for result_list_final in skils_list: # цикл делает запрос по каждому skils
        hh_api(result_list_final) # По России
        # hh_api(result_list_final, search_m)  # По Москве
        # hh_api(result_list_final, earch_k) # По Казани


found_sum = sum(found_list) # Общая сумма страниц, по каждому skils



for value in found_list: # Вычисляем проценты по каждому Skil
        procent = (value / found_sum) * 100
        procent_sum.append(float("{0:.3f}".format(procent)))# Объединяет каждый процент в один список  и сокращает до одной цыфры после запятой



general_list = list(zip(skils_list, procent_sum)) # Делаем список кортежей
general_list.sort(key=lambda a: a[1], reverse=True) # Сортирует по возрастанию процента

print('Skils', ' ' * 30 ,'%  \n')
for ele1,ele2 in general_list:
    print("{:<35}{:<11}".format(ele1,ele2))