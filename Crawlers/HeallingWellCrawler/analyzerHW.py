import json

with open('Crawlers/HeallingWellCrawler/testHealingWellThreads.json', 'r') as file:
    threadList = json.load(file)

len(threadList)
threadList[-1]