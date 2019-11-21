from bs4Test import redditThreadsCrawler as rTC
import multiprocessing

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=rTC.SearchThreads,
                                 args=("depression", 0))

    p2 = multiprocessing.Process(target=rTC.SearchComments,
                                 args=(p1.url))


    p1.join()
    p2.join()
