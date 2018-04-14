import praw
import time

reddit = praw.Reddit(client_id = 'cOrWaHLB_Hdidw', client_secret = '21usAKUK_6f7CbpKDhe-cQuinF4',
                    username = 'silaslfilho', password = 's140291f', user_agent = 'something')

subreddit = reddit.subreddit('depression')
#
hot_depression = subreddit.new(limit = 4)
#
for s in hot_depression:
 if not s.stickied:
     print('Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(s.title, s.ups, s.downs, s.visited, s.id))

     s.comments.replace_more(limit = 0)

     for comment in s.comments.list()[:15]:
        print(20*'-')
        print('Parent ID: ', comment.parent())
        print('Comment ID: ', comment.id())
        print(comment.body[:200])

hot_python = subreddit.hot(limit=3)
for submission in hot_python:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited?: {}, subid: {}'.format(submission.title,
                                                                                                   submission.ups,
                                                                                                   submission.downs,
                                                                                                   submission.visited,
                                                                                                   submission.id))
        submission.comments.replace_more(limit=0)
        # limiting to 15 results to save output
        for comment in submission.comments.list()[:15]:
            print(20*'#')
            print('Parent ID:',comment.parent())
            print('Comment ID:',comment.id)
            # limiting output for space-saving-sake, feel free to not do this
            print(comment.body[:200])
