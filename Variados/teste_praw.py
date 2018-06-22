import praw
import time

reddit = praw.Reddit(client_id = '', client_secret = '',
                    username = 'silaslfilho', password = '######', user_agent = 'something')

subreddit = reddit.subreddit('depression')
#
conversedict = {}
hot_depression = subreddit.hot(limit = 5)

for submission in hot_depression:
    if not submission.stickied:
        print('Title: {},"\n" Body: {},"\n" ups: {}, downs: {}, Have we visited?: {}, subid{}'.format(submission.title,
        submission.selftext,
        submission.ups,
        submission.downs,
        submission.visited,
        submission.id))

        submission.comments.replace_more(limit = 0)
        for comment in submission.comments.list():
            if comment.id not in conversedict:
                conversedict[comment.id] = [comment.body, {}]
                if comment.parent() != submission.id:
                    parent = str(comment.parent())
                    conversedict[parent][1][comment.id] = [comment.ups, comment.body]
            #
            # print(20*'#')
            # print('Parent ID:',comment.parent())
            # print('Comment ID:',comment.id)
            # print(comment.body[:200])

for s in hot_depression:
    if not s.stickied:
        print(s.title)


for post_id in conversedict:
    message = conversedict[post_id][0]
    replies = conversedict[post_id][1]
    if len(replies) > 1:
        print('Original Message: {}'.format(message))
        print(35*'_')
        print('Replies:')
        for reply in replies:
            print(replies[reply])

#------------------
subreddit = reddit.subreddit('news')

for comment in subreddit.stream.comments():
    try:
        print(30*'_')
        print()
        parent_id = str(comment.parent())
        submission = reddit.comment(parent_id)
        print('Parent:')
        print(submission.body)
        print('Reply')
        print(comment.body)
    except praw.exceptions.PRAWException as e:
        pass
