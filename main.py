from newsapi import NewsApiClient
import json
import pandas as pd
#from pandas.io.json import json_normalize
import config
from random import randint

#articleList = [(randint(1, 100)) for i in range(10)]

newsapi = NewsApiClient(api_key=config.API)

top_headlines = newsapi.get_top_headlines(category='business')
#print(type(top_headlines))
#print(top_headlines)
sources = newsapi.get_sources()

df = pd.DataFrame(list(top_headlines.items()), columns=['title', 'author'])


for i in range(5):
    randNum = (randint(0, 10))
    print(top_headlines['articles'][randNum]['title'])
    print(top_headlines['articles'][randNum]['source']['name'])


