import praw
import time

reddit = praw.Reddit(client_id = 'cOrWaHLB_Hdidw', client_secret = '21usAKUK_6f7CbpKDhe-cQuinF4',
                    username = 'silaslfilho', password = 's140291f', user_agent = 'something')

subreddit = reddit.subreddit('depression')
#
conversedict = {}
hot_depression = subreddit.hot(limit = 3)

for submission in hot_depression:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited?: {}, subid{}'.format(submission.title,
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

for post_id in conversedict:
    message = conversedict[post_id][0]
    replies = conversedict[post_id][1]
    if len(replies) > 1:
        print('Original Message: {}'.format(message))
        print(35*'_')
        print('Replies:')
        for reply in replies:
            print(replies[reply])
