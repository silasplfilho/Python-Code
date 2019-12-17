import json

with open("Crawlers/RedditCrawler/testRedditComments.json", 'r') as file:
    Commentsdataset = json.load(file)

#
len(Commentsdataset)
x = Commentsdataset[-1]
len(x)
x[0]['data']['body']