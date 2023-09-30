# сделать отоброжение всего поиск ('found')
# Сделать таблице по процентам skils
# Скорей всего нужно будет skils разъединять по отдельности и делать несколько поисков и потом только находить % от общего числа поиска


import requests
import pprint


def table():



# Поиск внутри hh
def hh_api(search):
        DOMAIN = 'https://api.hh.ru/'
        url_vacancies = f'{DOMAIN}vacancies'
        skils = 'Python OR PostgreSQL OR SQL OR ООП OR Git OR Unit Testing OR Flask OR FastAPI OR Redis OR API OR HTML OR arduino OR RabbitMQ OR Linux OR Django Framework OR PostgreSQL OR PyTorch OR scikit-learn OR NLP OR LLM OR BERT OR GPT OR ChatGPT OR OpenAI OR Atlassian Jira OR Scrum OR NoSQL OR TDD OR Redis OR Agile OR Scrapy OR CSS OR MS Visual Code OR BS4 OR Data Mining OR Beautifulsoupe OR XPath OR Базы данных OR JSON OR ML OR AI OR Big Data OR Разработка ПО OR MongoDB OR Data Analysis OR REST OR gRPC OR CSS OR JavaScript OR Docker OR Kafka OR Gitlab CI OR Openshift OR K8s'



        params= {
                'text': 'NAME: (python developer) OR DESCRIPTION:' f'{skils}', # NAME: вакансия DESCRIPTION: искать внутри вокансии
                'area': search,

                # создал страницу т.к. данных много
                'page': 1
        }
        result = requests.get(url_vacancies, params=params).json()

        pprint.pprint(result)

# items = result['items']
#
# first = items[0]
#
# pprint.pprint(first)

def osnov_menu():
        # 'area': 113, # Поиск по Рогссии
        #'area': 1624,  # Поиск по Казани
        # "'area': 1, # Поиск по Москве

        while True:
                print('1. Поиск по России')
                print('2. Поиск по Москве')
                print('3. Поиск по Казани')
                print('Иначе Выход ')
                choice = input('Выберите пункт меню: ')

                if choice == '1':
                        search = 113
                        hh_api(search)
                elif choice == '2':
                        search = 1
                        hh_api(search)

                elif choice == '3':
                        search = 1624
                        hh_api(search)
                else:
                        break


osnov_menu()