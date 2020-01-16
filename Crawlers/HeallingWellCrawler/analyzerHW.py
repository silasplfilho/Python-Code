import json
import jsonlines

threadList = []
commentList = []

with jsonlines.open('Crawlers/HeallingWellCrawler/HealingWellThreads.jsonl', mode='r') as file:
    for iter in file:
        threadList.extend(iter)


with jsonlines.open('Crawlers/HeallingWellCrawler/HealingWellComments_labCores.jsonl', mode='r') as file:
    for iter in file:
        commentList.extend(iter)

threadList[0]
commentList[0]