import json
import jsonlines

threadList = []
commentList = []

# --- Getting the list of forum posts
with jsonlines.open('Crawlers/HeallingWellCrawler/HealingWellThreads.jsonl', mode='r') as file:
    for iter in file:
        threadList.extend(iter)


with jsonlines.open('Crawlers/HeallingWellCrawler/HealingWellComments_labCores.jsonl', mode='r') as file:
    for iter in file:
        commentList.extend(iter)

# ---
sumComments = 0
for i in commentList:
    sumComments = sumComments + len(i)

len(threadList)