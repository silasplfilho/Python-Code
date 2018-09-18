from twitter_fetch.fetcher import fetch_loop

from twitter_fetch import persistence

persistence.DB = "yellowseptember"

query = "#worldsuicidepreventionday since:2018-09-01 until:2018-09-18"

fetch_loop(query)
