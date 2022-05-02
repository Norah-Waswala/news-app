from app import app
import urllib.request,json

from news_test import News
from .models import news

News = news.News
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news():
    get_news_url=base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data=url.read()
        get_news_response=json.loads(get_news_data)

        news_results=None

        if get_news_response['articles']:
            news_result_list=get_news_response["articles"]
            news_results=process_results(news_result_list)

    return news_results

def process_results(news_list):
    news_results=[]
    for news in news_list:
        
        author=news.get("author")
        title=news.get("title")
        description=news.get("description")
        urltoImage=news.get("urlToImage")
        date=news.get("date")
        content=news.get("content")
        url=news.get("url")
        if description and urltoImage:

            news_object=News(author,title,description,urltoImage,date,content,url)

            news_results.append(news_object)
            news_results=news_results[:6]
    return news_results