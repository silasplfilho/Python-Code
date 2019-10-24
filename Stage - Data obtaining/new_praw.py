from os.path import isfile
import praw
import pandas as pd
from time import sleep
import configparser
import datetime as dt

config = configparser.ConfigParser()
config.read('configuration.ini')

reddit = praw.Reddit(client_id=config['DEFAULT']['PRAW_client_id'], 
                     client_secret=config['DEFAULT']['PRAW_client_secret'],
                     username=config['DEFAULT']['username'],
                     password=config['DEFAULT']['PRAW_client_password'],
                     user_agent=config['DEFAULT']['user_agent'])
# ---
subr_depression = reddit.subreddit('depression')
depression_subms = subr_depression.new(limit=5)

topics_dict = {"title": [],
               "score": [],
               "id": [],
               "url": [],
               "comms_num": [],
               "created": [],
               "body": [],
               "author": []}
# ---
for submission in depression_subms:
    if not submission.stickied:
        topics_dict["title"].append(submission.title)
        topics_dict["body"].append(submission.selftext)
        topics_dict["id"].append(submission.id)
        topics_dict["score"].append(submission.score)
        topics_dict["created"].append(submission.created)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["author"].append(submission.author)
        topics_dict["url"].append(submission.url)
sleep(0.1)
# ---
dataset = pd.DataFrame(topics_dict)
dataset["creation"] = dataset["created"].apply(dt.datetime.fromtimestamp)

dataset.head()
# ---
with as:
	sample_author = dataset.loc[0, 'author']
	sample_author_comments = reddit.redditor(sample_author.name).comments.new(limit=None)

	subreddits_list = {}
	for i in sample_author_comments:
		subreddits_list.append(str(i.subreddit.display_name))


a = pd.Series(subreddits_list)
a.values

sample_author_comments = reddit.redditor(sample_author.name).friend_info
