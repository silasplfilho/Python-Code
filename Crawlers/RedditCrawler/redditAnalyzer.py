import json
import jsonlines

threadList = []
with jsonlines.open("Crawlers/RedditCrawler/threadList.jsonl", mode='r') as file:
    for obj in file:
        threadList.extend(obj)
    # Commentsdataset = json.loads(file)
cont = 0

for i in threadList:
    if i['data']['num_comments'] > 0:
        print(i)
        print("\n \n")
        cont = cont+1
cont
len(threadList)
threadList[8]['data']['num_comments']
json.load(threadList[0])
#

commentsList = []
with jsonlines.open("Crawlers/RedditCrawler/threadCommentsList.jsonl", mode='r') as file:
    for obj in file:
        commentsList.extend(obj)
    # Commentsdataset = json.loads(file)

len(commentsList)

commentsList[1]
