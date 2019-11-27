import requests
import json
# pacotes para controlar o tempo de requisicao das paginas
from time import sleep, time
from datetime import date
from random import random
# pacotes para trabalhar com threads e queues
from queue import Queue
from threading import Thread, Event


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


# FUNCAO PARA BUSCA DE CONTINUA DE THREADS NUM DETERMINADO SUBREDDIT
def SearchThreads(subRedditName, qtdDays):
    # ACRESCENTAR UM CONTROLE PARA SABER SE É A PRIMEIRA VEZ QUE SE RODA ESSA FUNÇÃO
    controlVariable = True
    pagingControl = None
    mainUrl = "https://www.reddit.com/r/" + subRedditName + "/new.json"

    while controlVariable is True:
        print("Buscando threads do subreddit: {}".format(subRedditName))

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

    # --------------------------------------------------------------------------------------------
        # - gravando a lista de threads/posts num arquivo .json
        writeThreadList2Json(threadList,)
        # print("Salvando as threads iniciais. Num total de {}".format(len(threadList)))
        # with open('bs4Test/testReddit.json', 'a+') as file:
        #     json.dump(threadList, file, indent=3, sort_keys=True)
            # TALVEZ ACRESCENTAR O JOB AQUI?????
    # --------------------------------------------------------------------------------------------
    # Funcao para aguardar uma quantidade determinada de tempo para uma nova requisicao
        timeSleep()

        # - Controle de continuação do 'while'
        lastElement = threadList[-1]
        timeControl = lastElement['data']['created_utc']
        timeControl = date.fromtimestamp(timeControl)

        actualDate = date.today()

        if (actualDate - timeControl).days > int(qtdDays):
            controlVariable = False
        else:
            continue

    return print("acabou")


def writeThreadList2Json(threadListObject, output_q):
    print("Salvando as threads iniciais. Num total de {}".format(len(threadListObject)))
    with open('bs4Test/testReddit.json', 'a+') as file:
        json.dump(threadListObject, file, indent=3, sort_keys=True)

        event = Event()
        output_q.put((threadListObject, event))
            # TALVEZ ACRESCENTAR O JOB AQUI?????


def SearchComments(threadInstance):
    url = threadInstance['data']['url']

    threadResponseJson = requests.get(url, headers={'User-agent': 'smthn'}).json()
    aux = threadResponseJson[1]['data']['children']

    print("Coletando comentários da thread {}.".format(url))
    print("Essa thread possui {} comments".format(len(aux)))

    threadInstance['comments'] = aux

    return aux
