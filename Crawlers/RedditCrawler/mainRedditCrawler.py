from Crawlers.RedditCrawler import redditThreadsCrawler as rTC
import multiprocessing

# queueObject.close()


if __name__ == "__main__":
    qtdDias = input("Digita a quantidade de dias que serão pesquisados:")

    queueObject = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=rTC.SearchThreads,
                                 args=(queueObject, "Depression", qtdDias))

    p2 = multiprocessing.Process(target=rTC.SearchandStoreCommentsQUEUE, args=(queueObject,))

    # with open('Crawlers/RedditCrawler/testRedditComments.json', 'a+', encoding='utf-8') as file:
    #     file.write('[')

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # with open('Crawlers/RedditCrawler/testRedditComments.json', 'a+', encoding='utf-8') as file:
    #     file.write(']')
