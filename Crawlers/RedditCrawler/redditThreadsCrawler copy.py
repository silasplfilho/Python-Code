import requests
import json
# pacotes para controlar o tempo de requisicao das paginas
from time import sleep, time
from datetime import date
from random import random
import os
# import multiprocessing
# pacotes para trabalhar com threads e queues
# import multiprocessing

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
"""
    Os endpoints abaixo sao opcoes ao que eu estou usando
    mainURL = "https://gateway.reddit.com/desktopapi/v1/subreddits/depression?rtj=only&\
    redditWebClient=web2x&app=web2x-client-production&include=prefsSubreddit"

    new_url = "https://gateway.reddit.com/desktopapi/v1/subreddits/depression?rtj=only&\
    redditWebClient=web2x&app=web2x-client-production&include=prefsSubreddit&dist=25&\
    layout=card&sort=new&geo_filter=BR"
    """
"""
ALGUMAS OBSERVACOES E MELHORIAS PARA O SCRIPT:
1 - nao esta funcionando o argumento 'dist'. Tento aumentar a quantidade de threads retornadas
pela requisicao
"""
# variaveis de teste nas 2as linhas abaixo
# subRedditName = "Depression"
# qtdDays = 0
# mainURL = "https://www.reddit.com/r/Depression/new.json"


# FUNCAO QUE FAZ O PROCESSO AGUARDAR UMA QUANTIDADE ALEATORIA DE SEGUNDOS ENTRE 1 E 4.
def timeSleep():
    # - variaveis para controle de tempo/sleep
    start_time = time()
    requestsControl = 0

    # - Tempo de espera para outra requisição
    requestsControl += 1
    sleep(random() * 3 + 1)  # - Escolhe um inteiro
    current_time = time()
    elapsed_time = current_time - start_time

    print('Request: {}; Frequency: {} requests/s'.format(requestsControl,
                                                         requestsControl/elapsed_time))


# Funcao abaixo é uma tentativa de usar multiprocessing.pipe
def SearchandStoreCommentsQUEUE(queueObject):
    # insert a control to know if the process already finished
    while True:
        threadsList = queueObject.get()

        for thread in threadsList:
            x = thread['data']
            if x['num_comments'] > 0:
                threadInstanceURL = (x['url'])
                print("Obtendo comentarios da thread {}".format(threadInstanceURL))
                threadResponseJson = requests.get((threadInstanceURL + ".json"),
                                                  headers={'User-agent': 'smthn'})
                threadResponseJson = json.loads(threadResponseJson.content)
                aux = threadResponseJson[1]['data']['children']
                print("Essa thread possui {} comments".format(len(aux)))
            else:
                continue

        # with open('Crawlers/RedditCrawler/testRedditComments.json', 'a') as file:
        #     json.dump(aux, file, indent=3, sort_keys=True)

        with open('Crawlers/RedditCrawler/testRedditComments.json', 'a+') as file:
            if os.stat(file.name).st_size <= 3:
                json.dump(aux, file, indent=3, sort_keys=True)
            else:
                file.write(',')
                json.dump(aux, file, indent=3, sort_keys=True)

        # if len(threadsList) < 0:
            # print("nao há mais thread a serem buscadas os comentarios")
            # break

        if queueObject.empty():
            print("nao há mais thread a serem buscadas os comentarios")
            queueObject.close()
            break

        # if (queueObject.empty()):
        #     print("queue object is empty")
        #     break
        # else:
        #     threadsList = queueObject.get()
        #     print(len(threadsList))

        #     for thread in threadsList:
        #         x = thread['data']
        #         if x['num_comments'] > 0:
        #             threadInstanceURL = (x['url'])
        #             print("Obtendo comentarios da thread {}".format(threadInstanceURL))
        #             threadResponseJson = requests.get((threadInstanceURL + ".json"),
        #                                               headers={'User-agent':    'smthn'})
        #             threadResponseJson = json.loads(threadResponseJson.content)
        #             aux = threadResponseJson[1]['data']['children']

        #     # print("Coletando comentários da thread {}.".format(url))
        #     print("Essa thread possui {} comments".format(len(aux)))
        #     with open('Crawlers/RedditCrawler/testRedditComments.json', 'a+') as file:
        #         json.dump(aux, file, indent=3, sort_keys=True)


def writeThreadList2Json(threadListObject, name2bsaved):
    print("Salvando {} threads".format(len(threadListObject)))
    with open('Crawlers/RedditCrawler/test' + name2bsaved + '.json', 'a') as file:
        json.dump(threadListObject, file, indent=3, sort_keys=True)


# FUNCAO PARA BUSCA DE CONTINUA DE THREADS NUM DETERMINADO SUBREDDIT
def SearchThreads(queueObject, subRedditName, qtdDays):
    # ACRESCENTAR UM CONTROLE PARA SABER SE É A PRIMEIRA VEZ QUE SE RODA ESSA FUNÇÃO
    controlVariable = True
    pagingControl = None
    mainUrl = "https://www.reddit.com/r/" + subRedditName + "/new.json"
    i = 0  # variavel de teste - limita a quantidade de vezes que vou executar a funcao

    print("Buscando threads do subreddit: {}".format(subRedditName))
    while controlVariable is True:
        if pagingControl is not None:
            # STAGE: ALTERAR A URL PARA ACRESCENTAR O VALOR DE CONTROLE AFTER
            print("The variable control current state is: {}".format(pagingControl))
            new_url = mainUrl + '?&after=' + pagingControl + '&limit=50'
            pageSource = requests.get(new_url, headers={'User-agent': 'smthn'}).json()
        else:
            # - Primeiro obtendo uma lista de threads da pagina inicial
            pageSource = requests.get(mainUrl, headers={'User-agent': 'smthn'}).json()

        # - valor para controlar a continuacao de threads no scroll down
        pagingControl = pageSource['data']['after']
        # - lista de threads na primeira paginacao
        threadList = pageSource['data']['children']

        # Gravando a lista de threads/posts num arquivo .json
        queueObject.put(threadList)
        writeThreadList2Json(threadList, "threadList")

        # Funcao para aguardar uma quantidade determinada de tempo
        timeSleep()

        # - Controle de continuação do 'while'
        # lastElement = threadList[-1]
        # timeControl = lastElement['data']['created_utc']
        # timeControl = date.fromtimestamp(timeControl)

        # actualDate = date.today()

        # if (actualDate - timeControl).days > int(qtdDays): comentando para fazer testes
        #     controlVariable = False
        if i == 0:
            controlVariable = False
        else:
            i = i+1
            continue

    return print("TODAS AS THREADS NO LIMITE DE TEMPO FORAM RECUPERADAS")

# ---
import multiprocessing
if __name__ == "__main__":
    qtdDias = input("Digita a quantidade de dias que serão pesquisados:")

    queueObject = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=SearchThreads,
                                 args=(queueObject, "Depression", qtdDias))

    p2 = multiprocessing.Process(target=SearchandStoreCommentsQUEUE, args=(queueObject,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

# # area de testes
mainUrl = "https://www.reddit.com/r/" + "Depression" + "/new.json"
pageSource = requests.get(mainUrl, headers={'User-agent': 'smthn'}).json()
pagingControl = pageSource['data']['after']
threadList = pageSource['data']['children']

# for t in threadList:
#     print(t['data']['num_comments'])
# threadList[0]
# url = "https://www.reddit.com/r/depression/comments/e51vnb/christmas/"
# threadResponseJson = requests.get((url + ".json"), headers={'User-agent': 'smthn'})
# threadResponseJson.content
with open("Crawlers/RedditCrawler/testRedditThreads.json", "r") as f:
    dataset = json.load(f)

y = dataset[3]
x = y['data']
x['num_comments'] > 0

for t in dataset:
    x = t['data']
    if x['num_comments'] > 0:
        threadInstanceURL = (x['url'])
        print("Obtendo comentarios da thread {}".format(threadInstanceURL))
        threadResponseJson = requests.get((threadInstanceURL + ".json"), headers={'User-agent': 'smthn'})
        thread = json.loads(threadResponseJson.content)

        aux = thread
        aux = json.dumps(aux, indent=3, sort_keys=True)
        print("Essa thread possui {} comments".format(len(aux)))

        genericDictionary = {'threadURL': threadInstanceURL, 'data': None}

    type(aux)

    with open('Crawlers/RedditCrawler/testRedditComments.json', 'w') as file:
        file.write('[')
        file.write('\n')
        file.write(']')

    with open('Crawlers/RedditCrawler/testRedditComments.json', 'a+', encoding='utf-8') as file:
        # genericDictionary['data'] = aux
        json.dump(genericDictionary, file, indent=3, sort_keys=True)
        # file.write(',')

json.dump()