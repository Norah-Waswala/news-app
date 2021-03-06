
from app import app
import urllib.request,json
from news_test import News
from .models import news,articles
News = news.News
# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
source_url= app.config['SOURCE_BASE_URL']
article_url = app.config['NEWS_ARTICLE_API']
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
    for news_item in news_list:
        author=news_item.get("author")
        title=news_item.get("title")
        description=news_item.get("description")
        urltoImage=news_item.get("urlToImage")
        date=news_item.get("publishedAt")
        content=news_item.get("content")
        url=news_item.get("url")
        if  urltoImage:
            news_object=News(author,title,description,urltoImage,date,content,url)
            news_results.append(news_object)
    return news_results
 # Getting various sources
def get_sources(sources):
    get_news_url=source_url.format(sources,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        source_data=url.read()
        source_response=json.loads(source_data)
        source_results=None
        if source_response["sources"]:
            new_source_results=source_response["sources"]
            source_results=process_sources(new_source_results)
    return source_results
def process_sources(source_list):
    source_results=[]
    for source in source_list:
        id=source.get("id")
        name=source.get("name")
        description=source.get("description")
        url=source.get("url")
        source_object=news.Sources(id,name,description,url)
        source_results.append(source_object)
    return source_results
'''
Fetching Articles
'''
def get_articles(name):
    get_articles_url=article_url.format(name,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        article_data=url.read()
        article_response=json.loads(article_data)
        article_object=None;
        if article_response['articles']:
            at_result_list=article_response["articles"]
            at_results=process_articles(at_result_list)
    return at_results
def process_articles(article_list):
    article_results=[]
    for article in article_list:
        title=article.get("title")
        description=article.get("description")
        urlToImage=article.get("urlToImage")
        url=article.get("url")
        publishedAt=article.get("publishedAt")
        article_object=articles.Articles(title,description,urlToImage,url,publishedAt)
        article_results.append(article_object)
    return article_results