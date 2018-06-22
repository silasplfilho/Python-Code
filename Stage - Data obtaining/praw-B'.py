import praw
import time
#--------------
# reddit possui as credenciais da minha conta no Reddit para usar o PRAW
#--------------
reddit = praw.Reddit(client_id = '', client_secret = '',
                    username = 'silaslfilho', password = '', user_agent = 'something')
#--------------
# defino os subreddits que obterei os dados
#--------------
subr_depression = reddit.subreddit('depression')
subr_mental_health = reddit.subreddit('mentalhealth')
subr_gett_over = reddit.subreddit('getting_over_it')
subr_suicide = reddit.subreddit('SuicideWatch')

#--------------
# defino uma variavel que recebe as postagens no reddit
# nelas eu posso restringir se serão as mais novas, ou mais comentadas, controversas (new, hot, rising, gilded, controversial, top)
# optarei pelas mais recentes
#--------------
depression_subms = subr_depression.new(limit = 50)
mentalhealth_subms = subr_mental_health.new(limit = 50)
gett_over_subms = subr_gett_over.new(limit = 50)
suicide_subms = subr_suicide.new(limit = 50)
#--------------
# posso definir dicionarios que guardarao as informações
#--------------
conversedict = {}
print(var)
print(depression_subms[1])
test = reddit.submission(id='8ixtde')
print(test.author)


for submission in depression_subms:
    if not submission.stickied:
        print('Title: {},"\n" Body: {},"\n" ups: {}, downs: {}, Have we visited?: {}, subid: {} \n\n'.format(submission.title,
        submission.selftext,
        submission.ups,
        submission.downs,
        submission.visited,
        submission.id,
        submission.url))

        ## submission.comments.replace_more(limit = 0)
        ## for comment in submission.comments.list():
        ##     if comment.id not in conversedict:
        ##         conversedict[comment.id] = [comment.body, {}]
        ##         if comment.parent() != submission.id:
        ##             parent = str(comment.parent())
        ##             conversedict[parent][1][comment.id] = [comment.ups, comment.body]
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
