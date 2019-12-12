import json

with open("Crawlers/RedditCrawler/testRedditComments.json", 'r') as file:
    dataset = json.load(file)


json.loads(dataset)