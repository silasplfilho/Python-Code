from bs4Test import redditThreadsCrawler as rTC
import json
# from queue import Queue
from multiprocessing import Pipe, Process


def threadCommentsControler(thread):
    threadNumberOfComments = thread['data']['num_comments']
    print(threadNumberOfComments)

    if threadNumberOfComments > 0:
        return thread


if __name__ == "__main__":
    qtdDias = input("Digita a quantidade de dias que serão pesquisados:")

    pipe1 = Pipe(True)
    p1 = Process(target=rTC.SearchThreads, args=(pipe1, 'depression', qtdDias))
    p1.start()

    pipe2 = Pipe(True)
    p2 = Process(target=rTC.SearchComments, args=(pipe1, pipe2, ))
    p2.start()

    with open('bs4Test/testReddit.json', 'r+') as file:
        threadList = json.load(file)
        for threadDictionary in file:
            url = threadCommentsControler(threadDictionary)
            p2 = Thread(target=rTC.SearchComments, args=(url))

            p1.start()
            p2.start()

            p1.join()
            p2.join()


# ---- area de testes
# with open('bs4Test/testReddit.json', 'r') as file:
#     threadList = json.load(file)

# threadList[0]