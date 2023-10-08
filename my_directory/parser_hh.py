# 1. Как получить набор навыков
# Поиск ваканси
import requests


# vacancy = 'NAME',input()
# address = input()
skill = []
temp = []
key_skills = []
skills = []



url = 'https://api.hh.ru/vacancies'
# 1. Параметры поиска
params = {
    'text': 'NAME:python',
    # есть страницы т.к. данных много
    'page': 1
}

result = requests.get(url, params=params).json()

# список вакансий
items = result['items']

for item in items:
    url = item['url']
    result = requests.get(url).json()
    # 2. Ключевые навыки
    key_skills = (result['key_skills'])
    # 3. Создать список всех ключевых навыков
    for i in key_skills:
        # 4. Убираем повторяющиеся ключевые навыки
        if i not in temp: temp.append(i)
        key_skills = temp



# 5ю Извлекаю из словоря и формирую в отдельный список
for elem in key_skills:
    skills.append(elem.get('name', None))
print(skills) # Список всех ключевых навыков

