# teste com library requests
import requests
import json

# pacotes para controlar o tempo de requisicao das paginas
from time import sleep, time
from random import random

# CRIANDO FUNCAO PARA BUSCAR COMENTARIOS


def SearchComments(url):
    threadResponseJson = requests.get(
        url, headers={'User-agent': 'smthn'}).json()
    aux = threadResponseJson[1]['data']['children']

    print("Coletando comentários da thread {}.".format(url))
    print("This thread has {} comments".format(len(aux)))

    return aux


# ----
# Primeiro obtendo uma lista de threads da pagina inicial
mainURL = "https://www.reddit.com/r/depression/new.json"
mainDocument = requests.get(mainURL, headers={'User-agent': 'smthn'}).json()

# valor para controlar a continuacao de threads no scroll down
pageControl = mainDocument['data']['after']
# lista de threads na primeira paginacao
threadList = mainDocument['data']['children']

with open('bs4Test/testReddit.json', 'w') as file:
    json.dump(threadList, file, indent=3, sort_keys=True)

# -----------
# lidando com o resultado
start_time = time()
requestsControl = 0

with open('bs4Test/testReddit.json', 'r+') as file:
    threadList = json.load(file)

for thread in threadList:
    threadData = thread['data']
    if threadData['num_comments'] > 0:
        threadUrl = str(threadData['url']).strip('/') + '.json'

        threadData['comments'] = SearchComments(threadUrl)
        # Tempo de espera para outra requisição
        requestsControl += 1
        sleep(random() * 3 + 1)  # Escolhe um inteiro
        current_time = time()
        elapsed_time = current_time - start_time
        # ---

with open('bs4Test/testReddit.json', 'w') as file:
    json.dump(threadList, file, indent=4, sort_keys=True)
# -----
# ACIMA - ETAPA INICIAL DE COLETA DE THREADS E COMENTARIOS DA PRIMEIRA PAGINA - CONCLUIDO
# AGORA O DESAFIO É FAZER O SCROLL DOWN

# -------------------------------
# accessing a thread link and getting its comments
# r2['kind']
# r3 = pd.DataFrame(r2['data'])
# r3.to_csv('bs4Test/DFredditTest.csv', sep='@')
# - COMENTARIOS SOBRE COMO PROCEDER A COLETA
"""
1 - Primeiro eu faço a coleta de uma lista inicial.
2 - Dessa lista inicial, faco duas coisas: (1-eu transformo os dados obtidos num dicionario),
                                           (2-obtenho uma variavel com o valor 'before', que
                                           controla a continuacao do scroll down)
3 - Apos coletar as threads da primeira pagina e seus comentarios, 
uso a variavel com o valor de 'before' para fazer uma nova requisicao
"""
# ------
# source.json()['data']['after']
# source.json()['data']['before']
# # -----------------
# mainURL = "https://www.reddit.com/r/depression/new.json"
# new_url = mainURL + '?&after=' + source.json()['data']['after'] + '&dist=100'
# page2 = requests.get(new_url, headers={'User-agent': 'smthn'})
# page2.json
# r = json.dumps(page2.json(), indent=2, sort_keys=True)
# page2.json()['data']

# page2.json()['data']['after']
# page2.json()['data']['before']
# r2 = page2.json()
# -----------------
"""
Lista de atributos a serem feita a persistencia num BD

threadDictionary["author"]
threadDictionary["author_fullname"]
threadDictionary["created"]
threadDictionary["created_utc"]
threadDictionary["downs"]
threadDictionary["id"]
threadDictionary["likes"]
threadDictionary["name"]
threadDictionary["num_comments"]
threadDictionary["num_crossposts"]
threadDictionary["permalink"]
threadDictionary["pinned"]
threadDictionary["score"]
threadDictionary["selftext"]
threadDictionary["subreddit"]
threadDictionary["subreddit_id"]
threadDictionary["subreddit_name_prefixed"]
threadDictionary["subreddit_subscribers"]
threadDictionary["title"]
threadDictionary["ups"]
threadDictionary["url"]
threadDictionary["user_reports"]
threadDictionary["view_count"]
threadDictionary["whitelist_status"]
"""
