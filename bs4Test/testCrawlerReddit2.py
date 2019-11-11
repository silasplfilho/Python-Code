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

threadDictionary









with open('bs4Test/testReddit.json', 'w') as file:
    json.dump(source.json(), file, indent=2, sort_keys=True)
# type(threadList)

source.json()['data']['after']
source.json()['data']['before']
# -----------------
mainURL = "https://www.reddit.com/r/depression/new.json"
new_url = mainURL + '?&after=' + source.json()['data']['after'] + '&dist=100'
page2 = requests.get(new_url, headers={'User-agent': 'smthn'})
page2.json
r = json.dumps(page2.json(), indent=2, sort_keys=True)
page2.json()['data']

page2.json()['data']['after']
page2.json()['data']['before']
r2 = page2.json()
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
