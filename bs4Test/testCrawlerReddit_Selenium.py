# teste com library requests
import requests
import json

# pacotes para controlar o tempo de requisicao das paginas
from time import sleep, time
from random import randint
# ----

mainURL = "https://www.reddit.com/r/depression/new.json"
source = requests.get(mainURL, headers={'User-agent': 'smthn'})

r = json.dumps(source.json(), indent=2, sort_keys=True)
source.json()['data']['after']
source.json()['data']['before']
# ----
mainURL = "https://www.reddit.com/r/depression/new.json"
new_url = mainURL + '?&after=' + source.json()['data']['after']

page2 = requests.get(new_url, headers={'User-agent': 'smthn'})

r = json.dumps(page2.json(), indent=2, sort_keys=True)
page2.json()['data']
# data = json.dumps(source.json, indent=2)
# urllib.parse.urlencode()















# x = source.json()['data']['children'][0]
# x['data']['title']


# mainDiv = soup.findAll("div", class_='rpBJOHq2PR60pnwJlUyP0')
# threadDiv = soup.find_all('div', class_=re.compile('^_1oQyIsiPHYt6nx7VOmd1sz'))

# type(mainDiv)
# threadDiv[0]

# for child in soup.descendants:
#     if child.name:
#         print(child.name)


# # ----
# childrenDiv = mainDiv.findAll('div', id=str.startswith("t3_dr4j"))

# len(childrenDiv)

# mainDiv.text
# lastPage = paging.findAll('a')[-1].get('href')
# pageNumber = int(lastPage.split('p=')[-1])  # numero da ultima pagina da comunidade analisada

# # criando uma lista, onde cada elemento é um dicionario/thread
# threadList = []  # Lista que guardara os posts
# dictLayout = dict()


# for pageIterator in range(3):
#     # definindo parametros a serem manipulados
#     threadURL = "https://www.healingwell.com/community/default.aspx?f=19&p={}".format(pageIterator)
#     source = requests.get(threadURL)
#     soup = BeautifulSoup(source.content)
#     # source = urllib.request.urlopen(URL).read()
#     # soup = BeautifulSoup(source, 'html.parser')

#     # ---
#     # tentando chegar direto no div que tem a informacao necessaria
#     focusedDiv = soup.find('div', class_='section-body-secondary')

#     threadDiv = soup.findAll('div', class_=re.compile("row fugazi forum-list"))
#     threadDiv[0].text.replace('^\n', '')

#     threadDiv[0].text
#     threadDiv[0].find('a', class_='forum-title').get('href')

#     # ---
#     for thread in threadDiv:
#         dictLayout['last_date'] = thread.find('div', class_='last-comment-date').text
#         dictLayout['author'] = thread.p.text
#         dictLayout['title'] = thread.a.text
#         dictLayout['views'] = thread.find('div', class_='views').text
#         dictLayout['link'] = thread.find('a', class_='forum-title').get('href')
#         # print(dictLayout)
#         threadList.append(dictLayout.copy())
# # -----------------------------------
# # provavelemte o controle de requests ira entrar aqui

# start_time = time()
# requestsControl = 0

# for postIterator in threadList:
#     # Trecho que faz a requisicao com requests
#     postLink = "https://www.healingwell.com" + postIterator['link']
#     source = requests.get(postLink)
#     soup = BeautifulSoup(source.content)

#     print("Getting information from post: {}; The status code was; {}".format(postLink, 
#                                                                               source.status_code))

#     # source = urllib.request.urlopen(postLink).read()
#     # soup = BeautifulSoup(source, 'html.parser')

#     sleep(randint(6, 11))  # Escolhe um inteiro entre 8 e 15

#     # Controle da requisicao
#     requestsControl += 1
#     sleep(randint(1, 3))
#     current_time = time()
#     elapsed_time = current_time - start_time
#     print('Request: {}; Frequency: {} requests/s'.format(requestsControl,
#                                                          requestsControl/elapsed_time))
#     clear_output(wait=True)

#     if source.status_code != 200:
#         warn('request: {}; Status code: {}'.format(requestsControl, source.status_code))

#     # Break the loop if the number of requests is greater than expected
#         if requestsControl > 72:
#             warn('Number of requests was greater than expected.')
#             break

#     # autor, timestamp e comentarios do post
#     smthng = soup.findAll(['a', 'div'], class_=['user-name', 'post-body', 'posted'])

#     threadComments = []
#     commentDict = dict()

#     for i in range(0, len(smthng), 3):
#         commentDict['commentAuthor'] = smthng[i].text  # Autor do Comentario
#         commentDict['commentTimestamp'] = smthng[i+1].text  # Data da publicacao
#         commentDict['comment'] = smthng[i+2].text  # Texto do Comentario

#         threadComments.append([commentDict['commentAuthor'],
#                                commentDict['commentTimestamp'],
#                                commentDict['comment']])

#     postIterator['postContent'] = threadComments
#     # print(postIterator['postContent'])

# # ---------------------------
# threadList[0]['last_date']
# len(threadList)
# with open('bs4Test/testHealingWell.json', 'w') as file:
#     json.dump(threadList, file)
# # type(threadList)


# # ---------------------------
