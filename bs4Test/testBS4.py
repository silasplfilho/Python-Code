# functions for reddit script


def searchComments(lengthThread, threadUrl):
    threadUrl = str(thread['url']).strip('/') + '.json'
    threadResponseJson = requests.get(threadUrl, headers={'User-agent': 'smthn'}).json()

    threadResponseJson[1]['data']
    threadResponseJson = threadResponseJson[1]['data']
    threadResponseJson[]
    # threadComments = threadResponseJson
    # threadResponseJson['before']

    thread['id']
    thread['comments'] = threadResponseJson['data']
