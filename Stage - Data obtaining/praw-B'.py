import praw
import os
import pandas as pd
import datetime as dt
import json

envVariable_client_id = os.environ.get('PRAW_client_id')
envVariable_client_secret = os.environ.get('PRAW_client_secret')
envVariable_password = os.environ.get('PRAW_password')

# --------------
# reddit possui as credenciais da minha conta no Reddit para usar o PRAW
# --------------
reddit = praw.Reddit(client_id=envVariable_client_id, client_secret=envVariable_client_secret,
                     username='JustTest4PRAW', password=envVariable_password, 
                     user_agent='something')
# --------------
# defino os subreddits que obterei os dados
# --------------
subr_depression = reddit.subreddit('depression')
subr_mental_health = reddit.subreddit('mentalhealth')
subr_gett_over = reddit.subreddit('getting_over_it')
subr_suicide = reddit.subreddit('SuicideWatch')

# --------------
# defino uma variavel que recebe as postagens no reddit
# nelas eu posso restringir se serão as mais novas, ou mais comentadas, controversas 
# (new, hot, rising, gilded, controversial, top)
# optarei pelas mais recentes
# --------------
depression_subms = subr_depression.new(limit=5)
mentalhealth_subms = subr_mental_health.new(limit=50)
gett_over_subms = subr_gett_over.new(limit=50)
suicide_subms = subr_suicide.new(limit=50)
# --------------
# posso definir dicionarios que guardarao as informações
# --------------
type(depression_subms)

topics_dict = {"title": [],
               "score": [],
               "id": [],
               "url": [],
               "comms_num": [],
               "created": [],
               "body": []}

for submission in depression_subms:
    if not submission.stickied:
        topics_dict["title"].append(submission.title)
        topics_dict["body"].append(submission.selftext)
        topics_dict["id"].append(submission.id)
        topics_dict["score"].append(submission.score)
        topics_dict["created"].append(submission.created)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["url"].append(submission.url)

dataset = pd.DataFrame(topics_dict)

dataset["created"] = dataset["created"].apply(dt.datetime.fromtimestamp)
